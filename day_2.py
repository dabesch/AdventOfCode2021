def move_func(data, aiming=False):
    depth = 0
    horizontal = 0
    aim = 0
    # I'm sure I can do better than stacking if statements...
    for direction, dist in data:
        if direction == 'forward':
            horizontal += int(dist)
            if aiming:
                depth += aim * int(dist)
        elif direction == 'down':
            if aiming:
                aim += int(dist)
            else:
                depth += int(dist)
        elif direction == 'up':
            if aiming:
                aim -= int(dist)
            else:
                depth -= int(dist)
    return depth * horizontal


data = open('data/day_2.txt').read().splitlines()
data = [d.split(' ') for d in data]
print('Part 1:', move_func(data))
print('Part 1:', move_func(data, aiming=True))
