class Car(object):

    def __init__(self, model,color,company,speed_limit):
        self.color = color
        self.company  = company
        self.model = model
        self.speed_limit = speed_limit


    def start(self):
        print("started")


    def stop(self):
        print("stopped " + self.model)

    def accelerate(self):
        print("accelerating..." + str(self.speed_limit))
        "accelerator functionality here"

    def change_gear(self, gear_type):
        print("gear changed")
        " gear related functionality here"


ferrari = Car("enzo", "red","ferrari ltd", 500)
rolls = Car("rr", "red","brit ltd", 500)



Car.start(ferrari)
Car.stop(rolls)
Car. accelerate(ferrari)
