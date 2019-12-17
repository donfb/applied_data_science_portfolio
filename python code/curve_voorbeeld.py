import numpy as np

in_values = np.array([5, 15, 19, 33, 69])
a = np.array([1, 2, 3, 10, 20, 30, 100, 200, 300])
b = a * 2
c = a[np.newaxis, :] - in_values[:, np.newaxis]
d = np.abs(c)
index_1 = d.argmin(axis=1)
index_2 = index_1 - 1
index_2[c[np.arange(in_values.shape[0]), index_1] < 0] += 2
a_1 = a[index_1]
a_2 = a[index_2]
difference_1 = np.abs(a_1 - in_values)
difference_2 = np.abs(a_2 - in_values)
difference = difference_1 + difference_2
value_1 = b[index_1]
value_2 = b[index_2]
out_value = (value_1 * difference_2 + value_2 * difference_1) / difference

print(out_value)
