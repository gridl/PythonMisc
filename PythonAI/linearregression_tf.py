import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

#define the number of points to generate
num_points = 1200

#Generate the data based on the equation y = mx + c

data = []
m = 0.2
c = 0.5

for i in range(num_points):
    # generate x
    x = np.random.normal(0.0,0.8)

    #generate some noise
    noise = np.random.normal(0.0,0.04)

    #compute y
    y = m*x + c + noise

    data.append([x,y])


#separate x and y
x_data = [d[0] for d in data]
y_data = [d[1] for d in data]

#plot
plt.plot(x_data,y_data,'ro')
plt.title('Input data')
plt.show()

#generate weights and biases
W = tf.Variable(tf.random_uniform([1],-1.0,1.0))
b = tf.Variable(tf.zeros([1]))

#define equation for 'y'
y  = W * x_data +b

#Define how to compute the loss
loss = tf.reduce_mean(tf.square(y-y_data))

#Define the gradient descent optimizer
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

#Initialize all the variables
init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

#Start iterating

num_iterations = 10
for step in range(num_iterations):
    sess.run(train)

    print('ITERATION', step+1)
    print('W = ',sess.run(W)[0])
    print('b =',sess.run(b)[0])
    print('loss = ', sess.run(loss))

    #Plot the input data
    plt.plot(x_data, y_data, 'ro')

    #Plot the predicted output line
    plt.plot(x_data,sess.run(W) * x_data + sess.run(b))

    plt.xlabel('Dimension 0')
    plt.ylabel('Dimension 1')

    plt.title('Iteration ' + str(step+1) + ' of ' + str(num_iterations))
    plt.show()
