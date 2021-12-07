def get_position(input_data, n, invert=False):
    bit_count = len(input_data)
    p0 = [d for d in input_data if d[n] == '0']
    val = len(p0) < bit_count / 2
    if len(p0) == bit_count / 2:
        val = True
    if invert:
        return str(int(not val))
    else:
        return str(int(val))


def filter_vals(data, invert=False):
    bit_count = len(data[0])
    for i in range(bit_count):
        most = str(get_position(data, i, invert))
        data = [d for d in data if d[i] == most]
        if len(data) == 1:
            break

    return int(data[0], 2)


data = open('data/day_3.txt').read().splitlines()
gamma = ''
epsilon = ''
for i in range(len(data[0])):
    gamma += get_position(data, i)
    epsilon += get_position(data, i, invert=True)
print('Part 1', int(gamma, 2) * int(epsilon, 2))

o2 = filter_vals(data)
co2 = filter_vals(data, True)
print('Part 2:', o2 * co2)
