from matplotlib import pyplot
import random



x_values = [0,4,6,7,8,4,5]
y_values = [random.randint(0,30) for elt in x_values]
pyplot.plot(x_values,y_values,"o-")
pyplot.ylabel("Values")
pyplot.xlabel("time")
pyplot.title("A title")
pyplot.show()