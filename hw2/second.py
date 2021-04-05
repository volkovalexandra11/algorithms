from collections import defaultdict
number = int(input())

sizes = [int(x) for x in input().split()]
frequency = {}
for size in sizes:
    if size not in frequency:
        frequency[size] = 0
    frequency[size] += 1

print(max(frequency.values()))
