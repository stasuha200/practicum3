import math
a = list(map(int, input().split()))
x = a[0]
y = a[1]
z = a[2]
alpha = math.acos((x ** 2 + y ** 2 - z ** 2) / (2 * x * y)) * (180/3.14)
beta = math.acos((x ** 2 + z ** 2 - y ** 2) / (2 * x * z)) * (180/3.14)
sigma = math.acos((z ** 2 + y ** 2 - x ** 2) / (2 * z * y)) * (180/3.14)
print(alpha, beta, sigma)
