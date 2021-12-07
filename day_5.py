from itertools import product


def horizontal_check(x1, y1, x2, y2):
    if x1 == x2:
        return True
    elif y1 == y2:
        return True
    else:
        return False


def process_data():
    data = open('data/day_5.txt').read().splitlines()
    data = [list(map(int, d.replace(' -> ', ',').split(','))) for d in data]
    h_data = [d for d in data if horizontal_check(*d)]
    d_data = [d for d in data if not horizontal_check(*d)]

    return h_data, d_data


def draw_line(x1, y1, x2, y2, diagonal=False):
    if diagonal:
        x_range = [i for i in range(x1, x2 + 1)]
        y_range = [i for i in range(y1, y2 + 1)]
        if x1 > x2:
            x_range = [abs(i) for i in range(-x1, x2 + 1)]
        if y1 > y2:
            y_range = [abs(i) for i in range(-y1, y2 + 1)]

        return [p for p in zip(x_range, y_range)]
    else:
        x_range = range(min(x1, x2), max(x1, x2) + 1)
        y_range = range(min(y1, y2), max(y1, y2) + 1)
        return [p for p in product(x_range, y_range)]


def draw_grid(data):
    max_x = max([max(h[0], h[2]) for h in data])
    max_y = max([max(h[0], h[2]) for h in data])
    grid = [[0 for i in range(max_x + 1)] for i in range(max_y + 1)]
    return grid


if __name__ == '__main__':
    h_data, d_data = process_data()
    grid = draw_grid(h_data)
    # print(grid)
    for coords in h_data:
        line = draw_line(*coords)
        for x, y in line:
            grid[y][x] += 1
    score = 0
    for row in grid:
        score += len([r for r in row if r > 1])

    print('Part 1 score:', score)
    for coords in d_data:
        line = draw_line(*coords, diagonal=True)
        for x, y in line:
            grid[y][x] += 1

    score = 0
    for row in grid:
        score += len([r for r in row if r > 1])

    print('Part 2 score:', score)
