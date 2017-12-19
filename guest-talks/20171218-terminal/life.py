from time import sleep

def dim(board):
    return (len(board), len(board[0]))

def get_nb_coords(board, i, j):
    m,n = dim(board)
    coords = [(i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]
    return ((x % m, y % n) for x,y in coords)

def count_living(board, coords):
    alive = 0
    for i,j in coords:
        alive += board[i][j]

    return alive

def count_live_nbs(board, i, j):
    coords = get_nb_coords(board, i, j)
    return count_living(board, coords)

def next_state(living, living_nbs):
    return int(2 <= living_nbs <= 3) if living else int(living_nbs == 3)

def next_cell_state(board, i, j):
    count = count_live_nbs(board, i, j)
    state = board[i][j] 
    return next_state(state, count)

def next_board(board):
    m,n = dim(board)
    return [[next_cell_state(board, i, j) for j in range(n)]
            for i in range(m)]

def row_to_string(row):
    return ''.join(['X' if x else ' ' for x in row])

def show(board, step):
    print('Step: {}'.format(step))
    row_strings = [row_to_string(row) for row in board]
    output = '\n'.join(row_strings)
    print(output)

def run(board, sleep_time=0.1):
    step = 0
    while True:
        step += 1
        show(board, step)
        sleep(sleep_time)
        board = next_board(board)

blinker = [[0,0,0,0,0],
        [0,0,0,0,0],
        [0,1,1,1,0],
        [0,0,0,0,0],
        [0,0,0,0,0]]

glider = [[0,0,0,0,0],
        [0,0,1,1,0],
        [0,1,0,1,0],
        [0,0,0,1,0],
        [0,0,0,0,0]]

if __name__ == '__main__':
    run(glider)
