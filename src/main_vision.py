# -*- coding: utf-8 -*-
"""
Created on Jun 29 2017 2:53 PM
@author: andrevaETH
"""

import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("../MNIST_data/", one_hot=True)


class Model():

    def __init__(self):
        """
        Constructor for the model
        """
        self.setup_placeholders()
        self.setup_variables()
        self.setup_model()
        self.setup_loss_function()
        self.setup_optimizer()

    def setup_placeholders(self):
        """
        Creates all placeholders
        """
        self.X = tf.placeholder(tf.float32, [None, 28, 28, 1])
        self.Y_ = tf.placeholder(tf.float32, [None, 10])

    def setup_variables(self):
        """
        Creates all variables
        """
        self.W = tf.Variable(tf.zeros([784, 10]))
        self.b = tf.Variable(tf.zeros([10]))
        self.init = tf.global_variables_initializer()

    def setup_model(self):
        """
        Creates the Model
        """
        self.Y = tf.nn.softmax(tf.matmul(tf.reshape(self.X, [-1, 784]), self.W) + self.b)

    def setup_loss_function(self):
        """
        Define the loss function
        """
        self.cross_entropy = -tf.reduce_sum(self.Y_ * tf.log(self.Y))

    def setup_optimizer(self):
        """
        Define the optimization function
        """
        self.optimizer = tf.train.GradientDescentOptimizer(0.003)
        self.train_step = self.optimizer.minimize(self.cross_entropy)


def main():
    # - Make Model object -
    nn_model = Model()

    # - Run the NN -
    sess = tf.Session()
    sess.run(nn_model.init)

    for i in range(1000):
        batch_X, batch_Y = mnist.train.next_batch(100)
        train_data = {nn_model.X: batch_X, nn_model.Y_: batch_Y}

        sess.run(nn_model.train_step, feed_dict=train_data)

        print("Run: " + str(i))

if __name__ == '__main__':
    main()
