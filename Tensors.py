import tensorflow as tf

# You can create Tensor objects with the `tf.constant` function:
x = tf.constant([[1, 2, 3, 4, 5]])
# You can create Tensor objects only consisting of 1s with the `tf.ones` function:
y = tf.ones((1, 5))
# You can create Tensor objects only consisting of 0s with the `tf.zeros` function:
z = tf.zeros((1, 5))
# You can use the `tf.range()` function to create Tensor objects:
q = tf.range(start=1, limit=6, delta=1)

print(x)
print(y)
print(z)
print(q)
