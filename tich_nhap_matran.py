def convolution(matrix, kernel):
    m, n = len(matrix), len(matrix[0])
    k, l = len(kernel), len(kernel[0])

    A = [[0] * (n - l + 1) for _ in range(m - k + 1)]
    for i in range(m - k + 1):
        for j in range(n - l + 1):
            tong = 0
            for ki in range(k):
                for kj in range(l):
                    tong += matrix[i + ki][j + kj] * kernel[ki][kj]
            A[i][j] = tong
    return A

mat_a = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

ker_b = [[2, 4],
         [1, 3]]


ketqua_convolution1 = convolution(mat_a, ker_b)
print("Câu 1:", ketqua_convolution1)

