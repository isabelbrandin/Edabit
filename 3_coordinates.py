def convert_cartesian(x_list, y_list):
    length = len(x_list)
    result = []
    for i in range(length):
        result.append([x_list[i], y_list[i]])
    
    return result

print(convert_cartesian([9, 8, 3], [1, 1, 1]))
