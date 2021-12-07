# data = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
data = open('data/day_7.txt').read()
data = list(map(int, data.split(',')))


def fuel_calc(data, fractal_fuel=False):
    data_size = max(data)
    if fractal_fuel:
        # Create lookup to speed up performance
        diff_lookup = [i + 1 for i in range(data_size)]
    results = [0 for i in range(data_size)]
    for i, v in enumerate(results):
        for val in data:
            diff = abs(i - val)
            if fractal_fuel:
                diff = sum(diff_lookup[:diff])
            results[i] += diff
    cheapest = min(results)
    return results.index(cheapest), cheapest


# part1
print('Part 1: position={} Fuel={}'.format(*fuel_calc(data)))
print('Part 2: position={} Fuel={}'.format(*fuel_calc(data, True)))
