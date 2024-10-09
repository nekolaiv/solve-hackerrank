def compareTriplets(a, b):
    lst = [0, 0]
    for i in range(max(len(a), len(b))):
        if a[i] > b[i]:
            lst[0] += 1
        elif a[i] < b[i]:
            lst[1] += 1
    return lst

# For testing only
print("Input numbers separated by spaces. Hit enter if done.")
a = list(map(int,input("a: ").rstrip().split()))
b = list(map(int,input("b: ").rstrip().split()))

result = compareTriplets(a, b)
print(*result)