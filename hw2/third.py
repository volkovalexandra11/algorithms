def is_homo(multi_set_inversed):
    return len(multi_set_inversed[2]) > 0


def is_hetero(multi_set_inversed):
    if (len(multi_set_inversed[1]) == 0
            and len(multi_set_inversed[2]) == 1):
        return False
    if len(multi_set_inversed[1]) == 1 and len(multi_set_inversed[2]) == 0:
        return False
    if len(multi_set_inversed[1]) == len(multi_set_inversed[2]) == 0:
        return False
    return True


def insert(multi_set: dict, multi_set_inversed: dict, el):
    if el not in multi_set:
        multi_set[el] = 0
    multi_set[el] += 1
    if multi_set[el] == 1:
        multi_set_inversed[1].add(el)
        return
    if multi_set[el] == 2:
        multi_set_inversed[2].add(el)
        multi_set_inversed[1].remove(el)
        return


def delete(multi_set: dict, multi_set_inversed: dict, el):
    if el not in multi_set:
        return
    if multi_set[el] > 2:
        multi_set[el] -= 1
        return
    if multi_set[el] == 2:
        multi_set_inversed[1].add(el)
        multi_set_inversed[2].remove(el)
        multi_set[el] -= 1
        return
    if multi_set[el] == 1:
        multi_set_inversed[1].remove(el)
        multi_set.pop(el)


multi_set = {}
multi_set_inversed = {
    1: set(),
    2: set()
}
commands = {
    'insert': insert,
    'delete': delete
}

content = open('homo.in', 'r').readlines()
to_write = open('homo.out', 'w')

number = int(content[0])

for i in range(1, number + 1):
    if i != number:
        line = content[i][:-1]
    else:
        line = content[i]
    command, el = line.split()
    el = int(el)
    commands[command](multi_set, multi_set_inversed, el)
    is_homogen = is_homo(multi_set_inversed)
    is_hetegen = is_hetero(multi_set_inversed)
    if is_hetegen and is_homogen:
        to_write.write('both')
        to_write.write('\n')
        continue
    if is_hetegen:
        to_write.write('hetero')
        to_write.write('\n')
        continue
    if is_homogen:
        to_write.write('homo')
        to_write.write('\n')
        continue
    to_write.write('neither')
    to_write.write('\n')
