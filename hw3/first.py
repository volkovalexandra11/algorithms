from time import perf_counter


def solve(line):
    start_index = 0
    end_index = len(line) - 1
    to_delete = set()

    while start_index < end_index:
        if start_index == end_index - 1 and line[start_index] == ')' and line[end_index] == '(':
            break

        if line[start_index] == '(' and line[end_index] == '(':
            end_index -= 1
            continue

        if line[start_index] == ')' and line[end_index] == ')':
            start_index += 1
            continue

        if line[start_index] == '(' and line[end_index] == ')':
            to_delete.add(start_index + 1)
            to_delete.add(end_index + 1)
            start_index += 1
            end_index -= 1
            continue

        if line[start_index] == ')' and line[end_index] == '(':
            start_index += 1
            end_index -= 1

    if len(to_delete) == 0:
        print(0)
        exit()

    print(1)
    print(len(to_delete))
    print(' '.join(map(str, sorted(to_delete))))


if __name__ == '__main__':
    line = input()
    solve(line)
