def z_func(s: str):
    z = [0] * len(s)
    left, right = 0, 0
    for i in range(1, len(s)):
        z[i] = max(0, min(z[i - left], right - i))
        while i + z[i] < len(s) and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > right:
            left, right = i, i + z[i]
    return z


def get_zeros_ones_count(s: str):
    zeros_count = 0
    ones_count = 0
    for digit in s:
        if digit == '0':
            zeros_count += 1
        else:
            ones_count += 1
    return zeros_count, ones_count


cur_timetable = input()
ideal_timetable = input()

cur_zeros_count, cur_ones_count = get_zeros_ones_count(cur_timetable)

ideal_z_values = z_func(ideal_timetable)
ideal_length = len(ideal_z_values)
max_pref_len = 0

for i in range(ideal_length - 1, ideal_length // 2 - 1, -1):
    if ideal_z_values[i] + i == ideal_length:
        if ideal_z_values[i] > max_pref_len:
            max_pref_len = ideal_z_values[i]

period = ideal_timetable[:(ideal_length - max_pref_len)] if max_pref_len != 0 else ideal_timetable
suffix = ideal_timetable[:max_pref_len] if max_pref_len != 0 else ''

period_zeros, period_ones = get_zeros_ones_count(period)
suffix_zeros, suffix_ones = get_zeros_ones_count(suffix)

res = []
while True:
    if period_ones > cur_ones_count or period_zeros > cur_zeros_count:
        break
    res.append(period)
    cur_ones_count -= period_ones
    cur_zeros_count -= period_zeros

if cur_zeros_count >= suffix_zeros and cur_ones_count >= suffix_ones:
    res.append(suffix)
    cur_ones_count -= suffix_ones
    cur_zeros_count -= suffix_zeros

if cur_ones_count != 0:
    res += ['1'] * cur_ones_count

if cur_zeros_count != 0:
    res += ['0'] * cur_zeros_count

print(''.join(res))
