from collections import defaultdict


def input_many_numbers():
    return [int(x) for x in input().split()]


VERY_BIG_PRICE = 5 * 10 ** 8


def input_all():
    input_many_numbers()
    all_prices = []

    for _ in range(4):
        line = input_many_numbers()
        all_prices.append(line)

    all_no_matching_comps = []

    for _ in range(3):
        count = int(input())
        mo_matching_for_type = defaultdict(set)
        for _ in range(count):
            first, second = input_many_numbers()
            mo_matching_for_type[second - 1].add(first - 1)

        all_no_matching_comps.append(mo_matching_for_type)

    return all_prices, all_no_matching_comps


def get_sorted_order(array):
    sorted_and_order = sorted((el, ind) for (ind, el) in enumerate(array))
    return [order for el, order in sorted_and_order]


def get_cheapest_comp(prices, all_no_matching_comps):
    bests = [prices[0]] + \
            [[VERY_BIG_PRICE] * count for count in map(len, prices[1:])]

    for component_type in range(1, 4):
        previous_bests = bests[component_type - 1]
        types_bests = bests[component_type]

        type_prices = prices[component_type]
        nm_for_type = all_no_matching_comps[component_type - 1]

        type_count = len(type_prices)
        previous_comp_type_count = len(previous_bests)

        sorted_index_by_cost_ascending = get_sorted_order(previous_bests)

        for comp_index in range(type_count):
            price = type_prices[comp_index]
            nm_for_comp = nm_for_type[comp_index]

            for prev_comp_index in range(previous_comp_type_count):
                if (sorted_index_by_cost_ascending[prev_comp_index]
                        not in nm_for_comp):
                    new_price = price + previous_bests[
                        sorted_index_by_cost_ascending[prev_comp_index]]
                    types_bests[comp_index] = new_price
                    break

    return min(filter(lambda cost: cost < VERY_BIG_PRICE, bests[-1]), default=-1)


if __name__ == '__main__':
    prices, no_matching = input_all()
    print(get_cheapest_comp(prices, no_matching))
