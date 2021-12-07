def depth_calc(data, tri=False):
    depths = [int(line) for line in data.splitlines()]
    if tri:
        # Part 2 split into triplets
        depths = [depths[i:i + 3] for i in range(len(depths))]
    inc_count = 0
    for i, d in enumerate(depths):
        if not tri and d > depths[i - 1] and i > 0:
            inc_count += 1
        elif tri and sum(d) > sum(depths[i - 1]) and i > 0 and len(d) == 3:
            inc_count += 1
    return inc_count


depth_data = open('data/day_1.txt').read()

# depth_data = [int(line) for line in depth_data.splitlines()]
print('Part 1:', depth_calc(depth_data))
print('Part 2:', depth_calc(depth_data, tri=True))
