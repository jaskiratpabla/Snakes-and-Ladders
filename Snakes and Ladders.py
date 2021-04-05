##
##=======================================================
## Jaskirat Pabla
## Snakes and Ladders
##=======================================================
##


import check


## Data Definition:

## A Board is a (listof (listof Str))
## Requires:
##     The length of the outer list is 10.
##     The length of each inner list is 10.
##     Each string is '.', 'L', or 'S'.


## Function used for testing purposes only
def empty_board():
    '''
    Returns a list of lists representing a Snakes and Ladders 
    board where each entry is a period.
    
    empty_board: None -> Board
    '''
    return list(map(lambda ignore: ["."]*10, range(10)))


## Constants for testing:
unchanged_test_board = empty_board()
A = [[1,20,21,40],[78,64],[50]]
B = [[99,82,79,62,59],[47,53,69]]
E = [[]]
H = list(map(lambda x: [x], list(range(101))))[1:]
C = list(map(lambda x: [x], list(range(51))))[1:]
D = list(map(lambda x: [x], list(range(50, 101))))[1:]
snakes_board = list(map(lambda ignore: ["S"]*10, range(10)))
ladders_board = list(map(lambda ignore: ["L"]*10, range(10)))
snake_ladder_board = (list(map(lambda ignore: ["L"]*10, range(5))) +
                      list(map(lambda ignore: ["S"]*10, range(5, 10))))
ladder_snake_board = (list(map(lambda ignore: ["S"]*10, range(5))) +
                      list(map(lambda ignore: ["L"]*10, range(5, 10))))


def flat_lst(lol):
    '''
    Returns a list of integers contaning all of the integers
    in each of the inner lists in lol.
    
    flat_lst: (listof (listof Nat)) -> (listof Nat)
    '''
    if (len(lol) == 0):
        return []
    else:
        return (lol[0] + flat_lst(lol[1:]))


def mutate_board(num, letter, game_board):
    '''
    Mutates game_board so that position num in game_board is
    replaced with letter.

    Effects: Mutates game_board.

    mutate_board: Nat (anyof "S" "L") Board -> None
    Requires: 1 <= num <= 100
    '''
    tens = (num // 10)
    ones = (num % 10)
    if (ones == 0):
        row = 10 - tens
        if ((num % 20) == 0):
            column = 0
        else:
            column = 9
    else:
        row = 9 - tens
        if ((tens % 2) == 0):
            column = ones - 1
        else:
            column = 10 - ones
    game_board[row][column] = letter


def make_board(snakes, ladders, board):
    '''
    Mutates board so each string becomes "S" or "L" if the number
    of the cell appears in snakes or ladders respectively, 
    otherwise board is unchanged.

    Effects: Mutates board.

    make_board: (listof (listof Nat)) (listof (listof Nat)) Board -> None
    Requires: - The integers in the inner lists of snakes and ladders must
                be between 1 to 100 (inclusive).
              - The integers in the inner lists of snakes and ladders must
                all be distinct across both nested lists.
    
    Examples:
        If test_board = empty_board() then
        make_board(E, E, test_board) => None
        and test_board is unchanged.
        
        If test_board = empty_board() then
        make_board(A, B, test_board) => None
        and test_board is mutated to:
        [['.', 'L', '.', '.', '.', '.', '.', '.', '.', '.'], \
         ['.', 'L', '.', '.', '.', '.', '.', '.', '.', '.'], \
         ['.', 'L', 'S', '.', '.', '.', '.', '.', '.', '.'], \
         ['.', 'L', '.', 'S', '.', '.', '.', '.', 'L', '.'], \
         ['.', 'L', '.', '.', '.', '.', '.', 'L', '.', '.'], \
         ['.', '.', '.', '.', '.', '.', 'L', '.', '.', 'S'], \
         ['S', '.', '.', '.', '.', '.', '.', '.', '.', '.'], \
         ['S', '.', '.', '.', '.', '.', '.', '.', '.', '.'], \
         ['S', '.', '.', '.', '.', '.', '.', '.', '.', '.'], \
         ['S', '.', '.', '.', '.', '.', '.', '.', '.', '.']]
    '''
    snakes = flat_lst(snakes)
    ladders = flat_lst(ladders)
    (list(map(lambda cell: mutate_board(cell, "S", board), snakes)))
    (list(map(lambda cell: mutate_board(cell, "L", board), ladders)))


## Examples:
test_board = empty_board()
check.expect("Ex 1 - snakes and ladders are lists of an empty list",
             make_board(E, E, test_board), None)
check.expect("Ex 1 Mutation", test_board, unchanged_test_board)

test_board = empty_board()
check.expect("Ex 2 - Typical", make_board(A, B, test_board), None)
check.expect("Ex 2 Mutation", test_board,
             [['.', 'L', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', 'L', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', 'L', 'S', '.', '.', '.', '.', '.', '.', '.'],
              ['.', 'L', '.', 'S', '.', '.', '.', '.', 'L', '.'],
              ['.', 'L', '.', '.', '.', '.', '.', 'L', '.', '.'],
              ['.', '.', '.', '.', '.', '.', 'L', '.', '.', 'S'],
              ['S', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['S', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['S', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['S', '.', '.', '.', '.', '.', '.', '.', '.', '.']])


## Tests:
test_board = empty_board()
check.expect("T1 - Mutate test_board to snakes_board",
             make_board(H, E, test_board), None)
check.expect("T1 Mutation", test_board, snakes_board)

test_board = empty_board()
check.expect("T2 - Mutate test_board to ladders_board",
             make_board(E, H, test_board), None)
check.expect("T2 Mutation", test_board, ladders_board)

test_board = empty_board()
check.expect("T3 - Mutate test_board to be half full snakes then ladders",
             make_board(C, D, test_board), None)
check.expect("T3 Mutation", test_board, snake_ladder_board)

test_board = empty_board()
check.expect("T4 - Mutate test_board to be half full ladders then snakes",
             make_board(D, C, test_board), None)
check.expect("T4 Mutation", test_board, ladder_snake_board)

test_board = empty_board()
check.expect("T5 - Typical", make_board(B, A, test_board), None)
check.expect("T5 Mutation", test_board,
             [['.', 'S', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', 'S', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', 'S', 'L', '.', '.', '.', '.', '.', '.', '.'],
              ['.', 'S', '.', 'L', '.', '.', '.', '.', 'S', '.'],
              ['.', 'S', '.', '.', '.', '.', '.', 'S', '.', '.'],
              ['.', '.', '.', '.', '.', '.', 'S', '.', '.', 'L'],
              ['L', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['L', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['L', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['L', '.', '.', '.', '.', '.', '.', '.', '.', '.']])

test_board = empty_board()
check.expect("T6 - Snakes but no ladders",
             make_board(B, E, test_board), None)
check.expect("T6 Mutation", test_board,
             [['.', 'S', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', 'S', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', 'S', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', 'S', '.', '.', '.', '.', '.', '.', 'S', '.'],
              ['.', 'S', '.', '.', '.', '.', '.', 'S', '.', '.'],
              ['.', '.', '.', '.', '.', '.', 'S', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']])

test_board = empty_board()
check.expect("T7 - Ladders but no snakes",
             make_board(E, A, test_board), None)
check.expect("T7 Mutation", test_board,
             [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', 'L', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', 'L', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'L'],
              ['L', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['L', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['L', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['L', '.', '.', '.', '.', '.', '.', '.', '.', '.']])

test_board = empty_board()
check.expect("T8 - snakes and ladders are lists of empty lists",
             make_board([[], [], []], [[], [], [], []], test_board), None)
check.expect("T8 Mutation", test_board, unchanged_test_board)

test_board = empty_board()
check.expect("T9 - snakes and ladders are empty lists",
             make_board([], [], test_board), None)
check.expect("T9 Mutation", test_board, unchanged_test_board)
