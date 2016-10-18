# Pythonic collections, comprehensions and generators

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self,it):
        self.items.append(it)

    def __iter__(self):
        #return self.items.__iter__()
        sorted_items = sorted(self.items, key= lambda i: -i.price)
        return sorted_items.__iter__()
        



class CartItem:
    def __init__(self, name, price):
        self.price = price
        self.name = name



cart = ShoppingCart()
cart.add_item(CartItem("guitar", 799))
cart.add_item(CartItem("cd", 19))
cart.add_item(CartItem("iphone",  699))


# can we do it for-in the cart?
print("Items in your cart")
# below wont work without the __iter__ method ( error given would be "shopping cart is not iterable")
for item in cart:
    print(" * {} ${}".format(item.name,item.price))


# what if it was to be sorted?
# sort and hend them back