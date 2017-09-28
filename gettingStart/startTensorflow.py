#!/usr/bin/env python  
#coding:utf-8  
import tensorflow as tf
print(tf.__version__)
node1 = tf.constant(3.0, dtype=tf.float32)
node2 = tf.constant(4.0) # also tf.float32 implicitly
print(node1, node2)
