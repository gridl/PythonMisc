# create three objects in the ORM layer Customer, Cheese, Purchase

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Date, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
# Table creation

from sqlalchemy import create_engine
engine = create_engine('sqlite://')

Base = declarative_base() #metaclass that intercepts the creation of each mapped table in the ORM and defines a coressponding table in the core layer





class Customer(Base): # Objects in the ORM layer inherit from the declarative base
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    def __repr__(self):
        return "<Customer(name='%s')>" % (self.name)


purchases_cheeses = Table( # unmapped table in the core layer - its not a class and not derived from the declarative base
    #will correspond to the table purchases_cheeses in the database and existins to provide the manytomany mappings betwwen cheeses and purchase IDs
    'purchases_cheeses', Base.metadata,
    Column('purch_id', Integer, ForeignKey('purchases.id', primary_key=True)),
    Column('cheese_id', Integer, ForeignKey('cheeses.id', primary_key=True))
        )

class Cheese(Base): # compare with Cheese - a mpped table in the ORM layer. Under the hood Cheese.__table__ is created in the core layer.Correspond to a table named cheeses in the DB
    __tablename__ = 'cheeses'
    id = Column(Integer, primary_key=True)
    kind = Column(String, nullable=False)
    purchases= relationship('Purchase', secondary='purchases_cheeses', back_populates='cheeses') #defines the realtionship between mapped classes Cheese and Purchase, they are related indirectly
    # through the secondary table purchases_cheeses (as opposed to directly via a ForeignKey
    #     back_populates adds an event listener so that when a new Purchase object is added to Cheese.purchases, the Cheese object will also appear in Purchase.cheeses.
    def __repr__(self):
        return "<Cheese(kind='%s')>" % (self.kind)

class Purchase(Base):
    __tablename__ = 'purchases'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id', primary_key=True))
    purchase_date = Column(Date, nullable=False)
    customer = relationship('Customer')
    cheeses = relationship('Cheese', secondary='purchases_cheeses', back_populates='purchases')

    def __repr__(self):
        return("<Purchase(customer='%s', dt='%s')>" % (self.customer.name, self.purchase_date))

# Tables are explicitly created by the declarative base
Base.metadata.create_all(engine)

# now the interaction using objects in the ORM layer

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
sess = Session()

leicester = Cheese(kind='Red Leicester')
camembert = Cheese(kind='Camembert')
sess.add_all((camembert, leicester))
cat = Customer(name='Cat')
sess.add(cat)
sess.commit()

import datetime
d = datetime.date(1971,12,18)
p = Purchase(purchase_date=d, customer=cat)
p.cheeses.append(camembert)
sess.add(p)
sess.commit()


#query the data

for row in sess.query(Purchase,Cheese).filter(Purchase.cheeses):
    print(row)

