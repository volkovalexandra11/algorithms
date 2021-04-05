from collections import defaultdict

set_count = int(input())
properties_by_name = {}

for _ in range(set_count):
    line = input().split()
    name = line[0][:-1]
    props = set(sorted(line[1:]))
    properties_by_name[name] = props

query_count = int(input())

for _ in range(query_count):
    to_intersect = input().split()
    result = properties_by_name[to_intersect[0]]
    for name in to_intersect:
        result = result.intersection(properties_by_name[name])

    if result:
        print(' '.join(sorted(result)))
    else:
        print('No solution.')
