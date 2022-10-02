# chessBoard = {'1h': 'bking', '1a': 'wqueen', '8d': 'bpwan','ff':'ff', '1v':'mm'}
chessBoard = {'1h': 'bking', '1a': 'wqueen', '8d': 'bpwan', '3c': 'bqueen', 'bpwan': '5c'}

def validateTile(tile):
    if(not tile[0].isdigit()):
        return False
    if(int(tile[0]) < 1 and int(tile[0]) > 8):
        return False
    if(tile[1] not in 'abcdefgh'):
        return False
    return True

def validatePiece(piece):
    pieceType = piece[1:]
    if(pieceType not in ['king', 'queen', 'pwan', 'rook']):
        return False
    return True

def validatePieceCount(pieces):
    validCount = {
        'king': (1,1),
        'queen': (0,1),
        'pwan': (0,8),
        'rook': (0,2)
    }
    count = {}
    for coloredPiece in pieces:
        piece = coloredPiece[1:]
        count.setdefault(piece, 0)
        count[piece] = count[piece] + 1 


def isValidChessBoard(chessBoard):
    # for tile,piece in chessBoard.items():
    #     isValidTile = validateTile(tile)
    #     if(not isValidTile):
    #         return False
    #     isValidPiece = validatePiece(piece)
    #     if(not isValidPiece):
    #         return False
    isPiecesCountValid = validatePieceCount(chessBoard.values())
    return True

print('result is: ' + str(isValidChessBoard(chessBoard)))