def hourglassSum(arr):
    max_sum = float('-inf')  # Initialize to the smallest possible value

    # Loop through possible hourglass top-left corners
    for i in range(len(arr) - 2):
        for j in range(len(arr) - 2):
            # Calculate the hourglass sum directly
            arr_sum = (
                arr[i][j] + arr[i][j + 1] + arr[i][j + 2] +  # Top row
                arr[i + 1][j + 1] +  # Middle
                arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]  # Bottom row
            )
            # Update max_sum if current arr_sum is greater
            if arr_sum > max_sum:
                max_sum = arr_sum

    return max_sum

if __name__ == '__main__':
    arr = [
        [-1, -1, 0, -9, -2, -2],
        [-2, -1, -6, -8, -2, -5],
        [-1, -1, -1, -2, -3, -4],
        [-1, -9, -2, -4, -4, -5],
        [-7, -3, -3, -2, -9, -9],
        [-1, -3, -1, -2, -4, -5]
    ] # Sample List
    result = hourglassSum(arr)
    print(f"Final: {result}")