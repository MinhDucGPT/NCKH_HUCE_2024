def convolution(matrix, kernel):
    m, n = len(matrix), len(matrix[0])
    p, q = len(kernel), len(kernel[0])
    B = [[0] * (n - q + 1) for _ in range(m - p + 1)]

    for i in range(m - p + 1):
        for j in range(n - q + 1):
            tong = 0
            for ki in range(p):
                for kj in range(q):
                    tong += matrix[i + ki][j + kj] * kernel[ki][kj]
            B[i][j] = tong
    return B

mat_a = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

ker_c = [[1, 1, 1],
         [0, 0, 0],
         [1, 1, 1]]


convolution2 = convolution(mat_a, ker_c)
print("Câu 2:", convolution2)
