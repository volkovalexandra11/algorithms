def prefix(s):
    p = [0] * len(s)
    for i in range(1, len(s)):
        k = p[i - 1]
        while k > 0 and s[k] != s[i]:
            k = p[k - 1]
        if s[k] == s[i]:
            k += 1
        p[i] = k
    return p


string = input()
prefix_values = prefix(string)
n = len(string)
if prefix_values[n - 1] == 0:
    print('Just a legend')
    exit()

last_pr = prefix_values[n - 1]
for i in range(n - 1):
    if prefix_values[i] == last_pr:
        print(string[:prefix_values[i]])
        exit()

next_pos_value = prefix_values[last_pr - 1]
if next_pos_value == 0:
    print('Just a legend')
    exit()

for i in range(n):
    a = prefix_values[i]
    if prefix_values[i] == next_pos_value and i != last_pr:
        print(string[:prefix_values[i]])
        exit()

# print('Just a legend')