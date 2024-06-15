def max_sliding_window(num_list, k):
    if not num_list or k <= 0:
        return []
    if len(num_list) <= k:
        return [max(num_list)]

    A = []
    for i in range(len(num_list) - k + 1):
        a = num_list[i:i + k]
        a_max = max(a)
        A.append(a_max)
    return A


# Ví dụ sử dụng:
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33,1]
k = 3
print(max_sliding_window(num_list, k))
