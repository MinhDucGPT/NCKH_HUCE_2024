def nearest_neighbor_interpolation(data):
    noi_suy = []
    for i in range(len(data)):
        if data[i] is None:
            j = i
            while data[j] is None:
                j -= 1
            noi_suy.append(data[j])
        else:
            noi_suy.append(data[i])
    return noi_suy

# Example usage
data = [1, 1.1, None, 1.4, None, 1.5, None, 2.0]
ketqua_noisuy = nearest_neighbor_interpolation(data)
print(ketqua_noisuy)
