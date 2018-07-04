import argparse
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def build_arg_parser():
    parser = argparse.ArgumentParser(description='build a CNN classfier')
    parser.add_argument('--input-dir', dest='input_dir',type=str,default='mnist_data', help='Data directory')
    return parser

def get_weights(shape):
    data = tf.truncated_normal(shape,stddev=0.1)
    return tf.Variable(data)

def get_biases(shape):
    data = tf.constant(0.1,shape=shape)
    return tf.Variable(data)

def create_layer(shape):
    W = get_weights(shape)
    b = get_biases([shape[-1]])

    return W,b

def convolution_2d(x,W):
    return tf.nn.conv2d(x,W,strides=[1,1,1,1],padding='SAME')

def max_pooling(x):
    return tf.nn.max_pool(x,ksize=[1,2,2,1], strides=[1,2,2,1],padding='SAME')

if __name__ == '__main__':
    args = build_arg_parser().parse_args()

    mnist = input_data.read_data_sets(args.input_dir, one_hot=True)
    #INPUT LAYER WITH 784 NEUROSN
    x = tf.placeholder(tf.float32,[None,784])
    # RESHAPE X INTO 4DTENSOR
    x_image = tf.reshape(x,[-1,28,28,1])
    #DEFINE FIRST CNN
    W_conv1,b_conv1 = create_layer([5,5,1,32])

    #Apply relu
    h_conv1 = tf.nn.relu(convolution_2d(x_image, W_conv1) + b_conv1)

    #apply max pooling
    h_pool1 = max_pooling(h_conv1)

    #define second conv layer
    W_conv2, b_conv2 = create_layer([5,5,32,64])

    h_conv2 = tf.nn.relu(convolution_2d(h_pool1,W_conv2) + b_conv2)

    h_pool2 = max_pooling(h_conv2)

    W_fc1, b_fc1 = create_layer([7*7&64,1024])

    h_pool2_flat = tf.reshape(h_pool2,[-1,7*7*64])

    h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat,W_fc1) + b_fc1)

    #define droppout layer to reduce overfitting

    keep_prob = tf.placeholder(tf.float32)
    h_fc1_drop = tf.nn.dropout(h_fc1,keep_prob)

    #readout layer
    W_fc2,b_fc2 = create_layer([1024,10])
    y_conv = tf.matmul(h_fc1_drop,W_fc2) + b_fc2


#Define the entropy loss and the optimizer
    y_loss = tf.placeholder(tf.float32,[None,10])
    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=y_conv, labels=y_loss))
    optimizer = tf.train.AdamOptimizer(1e-4).minimize(loss)

    predicted = tf.equal(tf.argmax(y_conv,1), tf.argmx(y_loss,1))
    accuracy = tf.reduce_mean(tf.cast(predicted, tf.float32))

    sess = tf.InteractiveSession()
    init = tf.global_variables_initializer()
    sess.run()

    num_iterations = 21000
    batch_size = 75
    print('Training the model...')
    for i in range(num_iterations):
        batch = mnist.train.next_batch(batch_size)

        if i %50 == 0:
            cur_accuracy = accuracy.eval(feed_dict={
                x:batch[0], y_loss: batch[1], keep_prob: 1.0})

        optimizer.run(feed_dict={x:batch[0],y_loss: batch[1], keep_prob:0.5})

    print('Test accuracy = ', accuracy.eval(feed_dict = {x:mnist.test.images,y_loss:mnist.test.labels}))










