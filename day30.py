import numpy as np

# 1. Creating Arrays

a = np.array([1, 2, 3, 4])

b = np.array([
    [1, 2],
    [3, 4]
])

c = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

d = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
]

print(a)
print(b)
print(c)

print(type(d))
print(type(c))

print(np.zeros(5))
print(np.ones((2, 3)))
print(np.arange(0, 10, 2))
print(np.linspace(0, 1, 5))


# 2. Array Properties

a = np.array([1, 2, 3, 4])

b = np.array([
    [1, 2],
    [3, 4]
])

c = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print("a shape:", a.shape)
print("a ndim:", a.ndim)
print("a size:", a.size)
print("a dtype:", a.dtype)

print()

print("b shape:", b.shape)
print("b ndim:", b.ndim)
print("b size:", b.size)
print("b dtype:", b.dtype)

print()

print("c shape:", c.shape)
print("c ndim:", c.ndim)
print("c size:", c.size)
print("c dtype:", c.dtype)


# 3. Indexing and Slicing

a = np.array([10, 20, 30, 40, 50])

print(a[0])
print(a[-1])
print(a[1:4])

b = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(b[0, 1])
print(b[:, 1])
print(b[1, :])
print(b[0:2, 1:3])


# 4. Array Calculations

a = np.array([1, 2, 3])

print("sum:", np.sum(a))
print("mean:", np.mean(a))
print("median:", np.median(a))
print("min:", np.min(a))
print("max:", np.max(a))
print("std:", np.std(a))


# 5. Boolean Filtering

a = np.array([10, 20, 30, 40, 50])

print(a > 25)
print(a[a > 25])
print(a[(a > 15) & (a < 45)])


# 6. Reshaping

a = np.arange(1, 7)

b = a.reshape(2, 3)

print(a)
print(b)

print(b.flatten())

b = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(b.T)


# 7. Matrix Operations

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print(A * B)
print(A @ B)
print(np.dot(A, B))
print(np.linalg.det(A))
print(np.linalg.inv(A))


# 8. Random Numbers

print(np.random.rand(3))
print(np.random.randint(1, 10, 5))
print(np.random.randn(3))


# 9. Broadcasting

a = np.array([1, 2, 3])

print(a * 10)

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(A + np.array([10, 20, 30]))