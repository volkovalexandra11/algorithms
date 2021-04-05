from collections import defaultdict

lines_count = int(input())
points_by_name = defaultdict(int)
all_changes = []

for _ in range(lines_count):
    name, diff = input().split()
    all_changes.append([name, diff])
    old_rating = points_by_name[name]
    points_by_name[name] += int(diff)


max_rating = max(points_by_name.values())
new_ratings = defaultdict(int)

for change in all_changes:
    name, diff = change
    new_ratings[name] += int(diff)
    if new_ratings[name] >= max_rating and points_by_name[name] == max_rating:
        print(name)
        exit()
