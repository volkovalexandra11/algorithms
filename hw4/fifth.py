def get_key(s: str):
    first = s[0]
    last = s[-1]
    sort = ''
    if len(s) > 2:
        letters = []
        for i in range(1, len(s) - 1):
            letters.append(s[i])
        sort = ''.join(sorted(letters))

    return first, last, sort


def first(iterable):
    for el in iterable:
        return el


if __name__ == '__main__':
    string = input()
    if len(string) == 1:
        print(string)
        exit()

    string = string[:-1]
    words = string.split()
    allowed_count = int(input())
    allowed_words = {}
    for _ in range(allowed_count):
        allowed = input()
        key = get_key(allowed)
        if key in allowed_words:
            allowed_words[key].add(allowed)
        else:
            allowed_words[key] = {allowed}

    resulting_str = []

    for word in words:
        wordKey = get_key(word)
        if wordKey in allowed_words:
            if word in allowed_words[wordKey]:
                resulting_str.append(word)
            else:
                resulting_str.append(first(allowed_words[wordKey]))

        else:
            print('No solution')
            exit()

    print(' '.join(resulting_str) + '.')
