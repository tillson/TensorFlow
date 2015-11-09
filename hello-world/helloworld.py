import tensorflow as tensor
hello = tensor.constant('Hello, TensorFlow!')
session = tensor.Session()
print session.run(hello)
a = tensor.constant(10)
b = tensor.constant(32)
print session.run(a + b)
