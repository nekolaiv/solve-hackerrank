def compareTriplets(a, b):
    score_a, score_b = 0, 0
    for x, y in zip(a, b):
        score_a += x > y
        score_b += x < y
    return [score_a, score_b]

# For testing only
print("Input numbers separated by spaces. Hit enter if done.")
a = list(map(int, input("a: ").rstrip().split()))
b = list(map(int, input("b: ").rstrip().split()))

result = compareTriplets(a, b)
print(*result)
