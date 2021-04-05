def power(base, exp, mod):
    if exp == 0:
        return 1
    if exp == 1:
        return base
    new_pow = exp // 2
    calc_pow = power(base, new_pow, mod)

    if exp % 2 == 0:
        return calc_pow * calc_pow % mod
    return (calc_pow * calc_pow % mod) * base % mod


original_line_len, pos_count = [int(x) for x in input().split()]
mod = 10 ** 9 + 7
substring = input()
length = len(substring)
start_positions = []

if pos_count != 0:
    start_positions = [int(x) for x in input().split()]

non_covering_count = 0
for i in range(pos_count):
    start = start_positions[i]
    end = start_positions[i] + length
    if end > original_line_len + 1:
        print(0)
        exit()
    if i == pos_count - 1:
        non_covering_count += end - start
        continue
    next_start = start_positions[i + 1]
    if end > next_start:
        difference = end - next_start
        if substring[:difference] != substring[-difference:]:
            print(0)
            exit()
    non_covering_count += min(next_start, end) - start

print(power(26, original_line_len - non_covering_count, mod))