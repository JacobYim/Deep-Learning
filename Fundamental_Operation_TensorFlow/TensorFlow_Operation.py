import tensorflow as tf

a = tf.constant(200)
b = tf.constant(300)

add_op = a + b

sess = tf.Session()
res = sess.run(add_op)

print(res)