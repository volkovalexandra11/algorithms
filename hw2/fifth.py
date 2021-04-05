intelligence_by_people = {}
intelligence_by_country = {}
max_days_by_country = {}
from_by_name = {}


# cur_max_country = ''


def get_cur_max_country():
    most_int_country_coef = max(intelligence_by_country.values())
    most_int_country = [c for c in intelligence_by_country
                        if intelligence_by_country[c] == most_int_country_coef]
    return most_int_country


def update_days():
    most_int = get_cur_max_country()
    if len(most_int) > 1:
        return
    cur_max_country = most_int[0]
    if cur_max_country not in max_days_by_country:
        max_days_by_country[cur_max_country] = 0
    max_days_by_country[cur_max_country] += 1
    return cur_max_country


def input_start_info():
    people_count = int(input())
    for _ in range(people_count):
        name, country, intelligence = input().split()
        int_coef = int(intelligence)
        intelligence_by_people[name] = int_coef
        if country not in intelligence_by_country:
            intelligence_by_country[country] = 0
        intelligence_by_country[country] += int_coef
        from_by_name[name] = country


def process_relocations():
    c_m_c = update_days()
    if c_m_c is None:
        was_max = False
    else:
        cur_max_country = c_m_c
        was_max = True
    days, relocation = [int(x) for x in input().split()]
    previous_day = 0
    for _ in range(relocation):
        day, name, destination = input().split()
        day = int(day)
        if was_max:
            max_days_by_country[cur_max_country] += (day - previous_day - 1)

        if destination not in intelligence_by_country:
            intelligence_by_country[destination] = 0
        intelligence_by_country[destination] += intelligence_by_people[name]

        cur = from_by_name[name]
        intelligence_by_country[cur] -= intelligence_by_people[name]
        from_by_name[name] = destination

        previous_day = day
        c_m_c = update_days()
        if c_m_c is None:
            was_max = False
            continue
        cur_max_country = c_m_c
        was_max = True

    a = 0
    if was_max:
        max_days_by_country[cur_max_country] += (days - previous_day - 1)


def get_sorted_order():
    most_int = set(max_days_by_country.keys())
    most_int = sorted(most_int)
    for c in most_int:
        print(c, max_days_by_country[c])


if __name__ == '__main__':
    input_start_info()
    process_relocations()
    # get_maximum_days_by_country()
    get_sorted_order()
    a = 0
