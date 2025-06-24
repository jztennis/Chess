import colorama
from colorama import Fore

# Knight = ♞
# King = ♚
# Queen = ♛
# Bishop = ♝
# Rook = ♜
# Pawn = ♙

# initialize colorama
colorama.init(autoreset=True)  # Initialize Colorama


# Parent
class Piece:
    def __init__(self, color):
        self.color = color


# Pawn Child
class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = '♙'
        self.not_moved = True

    def get_moves(self, curr_sq, board):
        moves = []
        if self.color == 'white':
            # pawn move forward
            if int(curr_sq[1]) + 1 <= 8 and board[curr_sq[0]][str(int(curr_sq[1]) + 1)] is None:
                moves.append(curr_sq[0] + str(int(curr_sq[1]) + 1))
            # pawn takes a column
            if curr_sq[0] == 'a':
                if int(curr_sq[1]) + 1 <= 8 and board[chr(ord(curr_sq[0]) + 1)][str(int(curr_sq[1]) + 1)] is not None and board[chr(ord(curr_sq[0]) + 1)][str(int(curr_sq[1]) + 1)].color != 'white':
                    moves.append(curr_sq[0] + 'x' + chr(ord(curr_sq[0]) + 1) + str(int(curr_sq[1]) + 1))
            # pawn takes h column
            elif curr_sq[0] == 'h':
                if int(curr_sq[1]) + 1 <= 8 and board[chr(ord(curr_sq[0]) - 1)][str(int(curr_sq[1]) + 1)] is not None and board[chr(ord(curr_sq[0]) - 1)][str(int(curr_sq[1]) + 1)].color != 'white':
                    moves.append(curr_sq[0] + 'x' + chr(ord(curr_sq[0]) - 1) + str(int(curr_sq[1]) + 1))
            # pawn takes inner columns
            else:
                if int(curr_sq[1]) + 1 <= 8:
                    if board[chr(ord(curr_sq[0]) + 1)][str(int(curr_sq[1]) + 1)] is not None and board[chr(ord(curr_sq[0]) + 1)][str(int(curr_sq[1]) + 1)].color != 'white':
                        moves.append(curr_sq[0] + 'x' + chr(ord(curr_sq[0]) + 1) + str(int(curr_sq[1]) + 1))
                    if board[chr(ord(curr_sq[0]) - 1)][str(int(curr_sq[1]) + 1)] is not None and board[chr(ord(curr_sq[0]) - 1)][str(int(curr_sq[1]) + 1)].color != 'white':
                        moves.append(curr_sq[0] + 'x' + chr(ord(curr_sq[0]) - 1) + str(int(curr_sq[1]) + 1))
            # adds 2 space first move
            if self.not_moved:
                moves.append(curr_sq[0] + str(int(curr_sq[1]) + 2))

        else:
            # pawn move forward
            if int(curr_sq[1]) - 1 > 0 and board[curr_sq[0]][str(int(curr_sq[1]) - 1)] is None:
                moves.append(curr_sq[0] + str(int(curr_sq[1]) - 1))
            # pawn takes a column
            if curr_sq[0] == 'a':
                if int(curr_sq[1]) - 1 > 0 and board[chr(ord(curr_sq[0]) + 1)][str(int(curr_sq[1]) - 1)] is not None and board[chr(ord(curr_sq[0]) + 1)][str(int(curr_sq[1]) - 1)].color != 'black':
                    moves.append(curr_sq[0] + 'x' + chr(ord(curr_sq[0]) + 1) + str(int(curr_sq[1]) - 1))
            # pawn takes h column
            elif curr_sq[0] == 'h':
                if int(curr_sq[1]) - 1 > 0 and board[chr(ord(curr_sq[0]) - 1)][str(int(curr_sq[1]) - 1)] is not None and board[chr(ord(curr_sq[0]) - 1)][str(int(curr_sq[1]) - 1)].color != 'black':
                    moves.append(curr_sq[0] + 'x' + chr(ord(curr_sq[0]) - 1) + str(int(curr_sq[1]) - 1))
            # pawn takes inner columns
            else:
                if int(curr_sq[1]) - 1 > 0:
                    if board[chr(ord(curr_sq[0]) + 1)][str(int(curr_sq[1]) - 1)] is not None and board[chr(ord(curr_sq[0]) + 1)][str(int(curr_sq[1]) - 1)].color != 'black':
                        moves.append(curr_sq[0] + 'x' + chr(ord(curr_sq[0]) + 1) + str(int(curr_sq[1]) - 1))
                    if board[chr(ord(curr_sq[0]) - 1)][str(int(curr_sq[1]) - 1)] is not None and board[chr(ord(curr_sq[0]) - 1)][str(int(curr_sq[1]) - 1)].color != 'black':
                        moves.append(curr_sq[0] + 'x' + chr(ord(curr_sq[0]) - 1) + str(int(curr_sq[1]) - 1))
            # adds 2 space first move
            if self.not_moved:
                moves.append(curr_sq[0] + str(int(curr_sq[1]) - 2))
        return moves


# Rook Child
class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.not_moved = True
        self.symbol = '♜'

    def get_moves(self, curr_sq, board):
        pass


# Knight Child
class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = '♞'

    def get_moves(self, curr_sq, board):
        pass


# Bishop Child
class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = '♝'

    def get_moves(self, curr_sq, board):
        pass


# Queen Child
class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = '♛'

    def get_moves(self, curr_sq, board):
        pass


# King Child
class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.not_moved = True
        self.symbol = '♚'

    def get_moves(self, curr_sq, board):
        pass


# ChessBoard
class ChessBoard:
    """Stores the Chessboard"""
    def __init__(self):
        self.board = {'a': {'1': Rook('white'), '2': Pawn('white'), '3': None, '4': None, '5': None, '6': None, '7': Pawn('black'), '8': Rook('black')},
                      'b': {'1': Knight('white'), '2': Pawn('white'), '3': None, '4': None, '5': None, '6': None, '7': Pawn('black'), '8': Knight('black')},
                      'c': {'1': Bishop('white'), '2': Pawn('white'), '3': None, '4': None, '5': None, '6': None, '7': Pawn('black'), '8': Bishop('black')},
                      'd': {'1': Queen('white'), '2': Pawn('white'), '3': None, '4': None, '5': None, '6': None, '7': Pawn('black'), '8': Queen('black')},
                      'e': {'1': King('white'), '2': Pawn('white'), '3': None, '4': None, '5': None, '6': None, '7': Pawn('black'), '8': King('black')},
                      'f': {'1': Bishop('white'), '2': Pawn('white'), '3': None, '4': None, '5': None, '6': None, '7': Pawn('black'), '8': Bishop('black')},
                      'g': {'1': Knight('white'), '2': Pawn('white'), '3': None, '4': None, '5': None, '6': None, '7': Pawn('black'), '8': Knight('black')},
                      'h': {'1': Rook('white'), '2': Pawn('white'), '3': None, '4': None, '5': None, '6': None, '7': Pawn('black'), '8': Rook('black')}
                      }
        self.turn = 'white'
        self.last_move = None

    def get_moves(self):
        moves = []
        for rank in self.board['a'].keys():
            for col in self.board.keys():
                piece = self.board[col][rank]
                if piece is not None:
                    try:
                        for move in piece.get_moves(f'{col}{rank}', self.board):
                            moves.append(move)
                    except Exception as ex:
                        print(ex)
                        continue
        print(moves)
        return moves

    def printboard(self):
        print('+----+----+----+----+----+----+----+----+')
        for rank in reversed(self.board['a'].keys()):
            print('| ', end='')
            for col in self.board.keys():
                if self.board[col][rank] is not None:
                    if self.board[col][rank].color == 'white':
                        print(Fore.WHITE + f'{self.board[col][rank].symbol}  | ', end='')
                    elif self.board[col][rank].color == 'black':
                        print(Fore.LIGHTBLACK_EX + f'{self.board[col][rank].symbol}  | ', end='')
                else:
                    print('   | ', end='')
            print('\n+----+----+----+----+----+----+----+----+')


'''
d4
Qd4
cxd4

d4+
Qd4+
cxd4+

'''


# MoveChecker
class MoveChecker:

    def check(self, move, board):
        if len(move) == 2:
            if move[0] >= 'a' and move[0] <= 'h' and move[1] >= '1' and move[1] <= '8':
                if board.board[move[0]][move[1]] is None:
                    return self.pawn(move, board)
                else:
                    return None
        elif len(move) == 3:
            if move[1] >= 'a' and move[1] <= 'h' and move[2] >= '1' and move[2] <= '8':
                if board.board[move[1]][move[0]] is None:
                    if move[0] == 'N':
                        return self.knight(move, board)
                    elif move[0] == 'B':
                        return self.bishop(move, board)
                    elif move[0] == 'R':
                        return self.rook(move, board)
                    elif move[0] == 'Q':
                        return self.queen(move, board)
                    elif move[0] == 'K':
                        return self.king(move, board)
                else:
                    return None

        elif len(move) == 4 and move[1] == 'x':
            if move[2] >= 'a' and move[2] <= 'h' and move[3] >= '1' and move[3] <= '8':
                if move[0] >= 'a' and move[0] <= 'h':
                    return self.pawn(move, board)
                if board.board[move[2]][move[3]] is not None:
                    # if move[0] >= 'a' and move[0] <= 'h':
                    #     return self.pawn(move, board)
                    if move[0] == 'N':
                        return self.knight(move, board)
                    elif move[0] == 'B':
                        return self.bishop(move, board)
                    elif move[0] == 'R':
                        return self.rook(move, board)
                    elif move[0] == 'Q':
                        return self.queen(move, board)
                    elif move[0] == 'K':
                        return self.king(move, board)
                else:
                    return None
        else:
            return None

    # def pawn(self, move, board):
    #     is_capture = 'x' in move
    #     turn = board.turn
    #     direction = 1 if turn == 'white' else -1
    #     start_rank = 2 if turn == 'white' else 7

    #     if is_capture:
    #         # Format: exd5
    #         from_file = move[0]
    #         to_file = move[2]
    #         to_rank = int(move[3])
    #         from_rank = str(to_rank - direction)

    #         # Check normal diagonal capture
    #         if board.board[to_file][str(to_rank)]:
    #             piece = board.board[from_file][from_rank]
    #             target_piece = board.board[to_file][str(to_rank)]
    #             if piece and piece[0] == '♙' and piece[1] == turn and target_piece[1] != turn:
    #                 return from_file + from_rank + to_file + str(to_rank)

    #         # En passant
    #         if not board.board[to_file][str(to_rank)] and board.last_move:
    #             lm_from_file = board.last_move[0]
    #             lm_from_rank = int(board.last_move[1])
    #             lm_to_file = board.last_move[2]
    #             lm_to_rank = int(board.last_move[3])

    #             if (
    #                 lm_from_file == to_file and
    #                 abs(lm_to_rank - lm_from_rank) == 2 and
    #                 board.board[to_file][str(from_rank)] and
    #                 board.board[to_file][str(from_rank)][0] == '♙' and
    #                 board.board[to_file][str(from_rank)][1] != turn
    #             ):
    #                 return from_file + from_rank + to_file + str(to_rank)

    #     else:
    #         # Format: d4
    #         file = move[0]
    #         rank = int(move[1])
    #         one_step = str(rank - direction)
    #         two_step = str(rank - 2 * direction)

    #         # One step forward
    #         if one_step in board.board[file]:
    #             piece = board.board[file][one_step]
    #             if piece and piece[0] == '♙' and piece[1] == turn:
    #                 return file + one_step + move

    #         # Two steps forward
    #         if rank == (4 if turn == 'white' else 5):
    #             if (
    #                 two_step in board.board[file] and one_step in board.board[file] and
    #                 board.board[file][one_step] is None
    #             ):
    #                 piece = board.board[file][two_step]
    #                 if piece and piece[0] == '♙' and piece[1] == turn:
    #                     return file + two_step + move

    #     print("Invalid pawn move.")
    #     return None

    def pawn(self, move, board):
        is_capture = 'x' in move
        turn = board.turn

        if is_capture:
            # e.g., move = 'exd4'
            from_file = move[0]
            to_file = move[2]
            to_rank = int(move[3])

            if turn == 'white':
                from_rank = str(to_rank - 1)
            else:
                from_rank = str(to_rank + 1)

            # Check if there's a pawn at the expected square
            if from_file in board.board and from_rank in board.board[from_file]:
                piece = board.board[from_file][from_rank]
                if piece and piece[0] == '♙' and piece[1] == turn:
                    # Confirm the target square has an opponent's piece
                    target_piece = board.board[to_file][str(to_rank)]
                    if target_piece and target_piece[1] != turn:
                        return from_file + from_rank + to_file + str(to_rank)

        else:
            # e.g., move = 'd4'
            file = move[0]
            rank = int(move[1])
            direction = 1 if turn == 'white' else -1
            # start_rank = 2 if turn == 'white' else 7

            one_step = str(rank - direction)
            two_step = str(rank - 2 * direction)

            # One step forward
            if one_step in board.board[file]:
                piece = board.board[file][one_step]
                if piece and piece[0] == '♙' and piece[1] == turn:
                    return file + one_step + move

            # Two steps forward from starting position
            if rank == (4 if turn == 'white' else 5):  # target rank is 4 (white) or 5 (black)
                if two_step in board.board[file] and one_step in board.board[file]:
                    piece = board.board[file][two_step]
                    if (piece and piece[0] == '♙' and piece[1] == turn and board.board[file][one_step] is None):
                        return file + two_step + move

        return None

    def rook(self, move, board):
        pass

    def bishop(self, move, board):
        pass

    def knight(self, move, board):
        pass

    def queen(self, move, board):
        pass

    def king(self, move, board):
        pass


def game():
    print("To Resign: 'resign'")
    # player_color = input('Color...')
    board = ChessBoard()
    board.get_moves()
    movechecker = MoveChecker()
    board.printboard()
    move = input('Move...')

    while move != 'resign':
        move = movechecker.check(move, board)
        board.move(move)
        board.printboard()
        print('Turn:', board.turn)
        move = input('Move...')


# ================ GAME ================ #
game()
