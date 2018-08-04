import tensorflow as tf

a = tf.constant(100)
b = tf.constant(10)
c = tf.constant(110)

calc1_op = a + c - b
calc2_op = (a + b) * c

sess = tf.Session()
res1 = sess.run(calc1_op)
print(res1)

res2 = sess.run(calc2_op)
print(res2)
