module = 10 ** 15 + 159
calc_hash = int(input())

for i in range(2**16, 2**17):
    bin_i = bin(i)[2:]
    k = 1
    s = 0
    for j in range(len(bin_i) - 1, 0, -1):
        s = (s + int(bin_i[j]) * k % module) % module
        k = k * 257 % module

    if s == calc_hash:
        print(s[1:])
        exit()

print('No')

