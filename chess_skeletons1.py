

class ChessBoard(object):
    """
    """
    def __init__(self, size=(8, 8), pieces=None, dead_pieces=None, board=None, mode="default"):
        """
        """
        self._pieces = pieces
        self._size = size # attributes retained by the class need the self reference also
        self._dead_pieces = dead_pieces
        self._board = board

        self._generate_board_state(mode=mode) # using functions for initialization can be good practice

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        repr_string = ""
        for rank in range(self._size[0]-1, -1, -1):
            repr_string += str(self._board[rank]) + "\n"
        return repr_string

    def _visualize(self, view="white"):
        vis_str = self.__repr__()

    def _get_size(self):
        return self._size # how to access class attributes some where else in the object

    def _generate_board_state(self, mode="default"):
        self._board = []
        for rank in range(self._size[0]):
            self._board.append([])
            for file_ in range(self._size[1]):
                if (rank + file_) %2 == 0:
                    self._board[rank].append(Square("black"))
                else:
                    self._board[rank].append(Square("white"))
        if mode == "default":
            self._generate_default_board()

    def _generate_default_board(self):
        self._pieces = {"white":[], "black":[]}
        self._dead_pieces = {"white":[], "black":[]}
        power_pieces = {0:Rook, 1:Knight, 2:Bishop, 3:Queen,
                        4:King, 5:Bishop, 6:Knight, 7:Rook}
        for rank in range(self._size[0]):
            for file_ in range(self._size[1]):
                if rank == 1:
                    color = 'white'
                    piece = Pawn(position=(rank, file_), color=color)
                elif rank == 6:
                    color = 'black'
                    piece = Pawn(position=(rank, file_), color=color)
                elif rank == 0:
                    color = 'white'
                    piece = power_pieces[file_](position=(rank, file_), color=color)
                elif rank == 7:
                    color = 'black'
                    piece = power_pieces[file_](position=(rank, file_), color=color)
                else:
                    piece = None
                if piece != None:
                    self._pieces[color].append(piece)

                self._board[rank][file_]._piece = piece


class Square(object):
    """
    """
    def __init__(self, color, piece=None):
        self._color = color
        self._piece = piece

    def __str__(self):
        if self._piece == None:
            return self._color[0]
        return str(self._piece)

    def __repr__(self):
        return self.__str__()


class Piece(object):    # truth be told, I don't know what (object) does because they all should inherit from object
    """
    """
    def __init__(self, position, color, ptype="piece", player=None): # abstract definition that can be called in child class
        """
        """
        self._position = position
        self._player = player
        self._color = color
        self._ptype = ptype

    def __str__(self):
        return self._ptype[0]

    def __repr__(self):
        return self.__str__()

    def _move(self):    # abstract definition to be oSverloaded
        pass

    def _attack(self):
        pass

    def _die(self):     # abstract method, may not be needed
        pass

    def _get_moves(self):
        pass


class Pawn(Piece):
    """
    """
    def __init__(self, position, color):
        """
        """
        super(Pawn, self).__init__(position=position, color=color, ptype="Pawn")    # calling parent init function


class Knight(Piece):
    """
    """
    def __init__(self, position, color):
        """
        """
        super(Knight, self).__init__(position=position, color=color, ptype="knight")   # this also give an instance the self._position attribute


class Bishop(Piece):
    """
    """
    def __init__(self, position, color):
        """
        """
        super(Bishop, self).__init__(position=position, color=color, ptype="Bishop")


class Rook(Piece):
    """
    """
    def __init__(self, position, color):
        """
        """
        super(Rook, self).__init__(position=position, color=color, ptype="Rook")


class Queen(Piece):
    """
    """
    def __init__(self, position, color):
        """
        """
        super(Queen, self).__init__(position=position, color=color, ptype="Queen")


class King(Piece):
    """
    """
    def __init__(self, position, color):
        """
        """
        super(King, self).__init__(position=position, color=color, ptype="King")


class Player(object):
    """Class player holds the methods for guided interactions with the board
    and pieces. This will be concrete in that the player can interact via
    the object, but abstract in that another class will inherit functionality
    but override relevant functions for agent interfacing

    attributes:

    methods:
    """
    def __init__(self): # note: every class function should use the 'self' reference
        """Class initialization method. This is called at object instantiation.
        Initial attributes are usually set here. Docstrings are usually used
        to describe functionality.
        """
        pass


class AgentPlayer(Player):
    """
    """
    def __init__(self):
        """
        """
        pass


if __name__ == "__main__": # this code only runs if you run this file (python chess_skeletons.py)
    chess_board0 = ChessBoard()             # instantiates a chess board
    print(chess_board0)
