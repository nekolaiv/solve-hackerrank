def hourglassSum(arr):
    final_arr_sum = []
    for i in range(len(arr) - 2):
        for j in range(len(arr) - 2):
            arr_sum = 0
            for k in range(i, i + 3):
                for m in range(j, j + 3):
                    if k == i + 1 and (m == j or m == j + 2):
                        continue
                    arr_sum += arr[k][m]
            final_arr_sum.append(arr_sum)
    return max(final_arr_sum)
        

if __name__ == '__main__':
    arr = [
        [-1, -1, 0, -9, -2, -2],
        [-2, -1, -6, -8, -2, -5],
        [-1, -1, -1, -2, -3, -4],
        [-1, -9, -2, -4, -4, -5],
        [-7, -3, -3, -2, -9, -9],
        [-1, -3, -1, -2, -4, -5]
    ] # Sample Array
    result = hourglassSum(arr)
    print(f"Final: {result}")

