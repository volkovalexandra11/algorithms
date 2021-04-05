sets_count = int(input())
intersections_count = int(sets_count * (sets_count - 1) / 2)
result = set()
previous = frozenset([x for x in input().split()][1:])

if sets_count == 2:
    previous = list(previous)
    print(1, previous[0], sep=' ')
    print(len(previous) - 1, ' '.join(previous[1:]), sep=' ')
    exit()

for set_set in range(intersections_count - 1):
    inp = [x for x in input().split()]
    if inp[0] != 0:
        current = frozenset(inp[1:])
        intersection = previous.intersection(current)
        difference = previous - intersection
        prev_difference = current - intersection
        if len(difference) and len(intersection):
            result.add(difference)
        if len(prev_difference) and len(intersection):
            result.add(prev_difference)
        if len(intersection):
            result.add(intersection)

for set_set in result:
    print(len(set_set), ' '.join(list(set_set)), sep=' ')
