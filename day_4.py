import copy


def process_data():
    data = open('data/day_4.txt').read().splitlines()
    entries = list(map(int, data[0].split(',')))
    boards = []
    i = 2
    while True:
        b_data = data[i:i + 5]
        b_data = [b.replace('  ', ' ').strip().split(' ') for b in b_data]
        b_data = [list(map(int, b)) for b in b_data]
        boards.append(b_data)
        i += 6
        if i > 597:
            break
    return entries, boards


def bingo_call(n, board):
    new_board = []
    for row in board:
        if n in row:
            row.remove(n)
        new_board.append(row)
    return new_board


def score_board(board_round, number):
    remaining_board_score = sum([sum(row) for row in board_round])
    return remaining_board_score * number


def run_bingo(boards, entries):
    bingo_boards = copy.deepcopy(boards)
    results = []
    complete = []
    # This loop should get sorted
    for rnd, number in enumerate(entries):
        for i, board in enumerate(bingo_boards):
            if i not in complete:
                board_round = bingo_call(number, board)
                bingo_boards[i] = board_round
                if [] in board_round:
                    results.append(score_board(board_round, number))
                    complete.append(i)
    return results


entries, boards = process_data()

bingo_results = run_bingo(boards, entries)
last_idx = len(bingo_results) - 2
print(f'Part 1:{bingo_results[0]}', f'Part 2:{bingo_results[last_idx]}')
