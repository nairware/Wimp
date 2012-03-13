#board state must have following things:
#1. piece list (each piece has a color/side, type, and position)
#2. whose turn it is to move
#3. castling disqualification details

class Piece:
  p_color = "X"
  p_type = "X"
  p_rank = 0
  p_file = 0

class BoardState:
  piece_list = []
  player_turn = "X"
  castling_rights = [True, True, True, True]

board_state = BoardState()
  
for i in range(32):
  board_state.piece_list.append(Piece())

def PlacePiece(p, c, t, r, f):
  p.p_color = c
  p.p_type = t
  p.p_rank = r
  p.p_file = f

#setup new game
PlacePiece(board_state.piece_list[0], "W", "R", 1, 1)
PlacePiece(board_state.piece_list[1], "W", "N", 1, 2)
PlacePiece(board_state.piece_list[2], "W", "B", 1, 3)
PlacePiece(board_state.piece_list[3], "W", "Q", 1, 4)
PlacePiece(board_state.piece_list[4], "W", "K", 1, 5)
PlacePiece(board_state.piece_list[5], "W", "B", 1, 6)
PlacePiece(board_state.piece_list[6], "W", "N", 1, 7)
PlacePiece(board_state.piece_list[7], "W", "R", 1, 8)
PlacePiece(board_state.piece_list[8], "W", "P", 2, 1)
PlacePiece(board_state.piece_list[9], "W", "P", 2, 2)
PlacePiece(board_state.piece_list[10], "W", "P", 2, 3)
PlacePiece(board_state.piece_list[11], "W", "P", 2, 4)
PlacePiece(board_state.piece_list[12], "W", "P", 2, 5)
PlacePiece(board_state.piece_list[13], "W", "P", 2, 6)
PlacePiece(board_state.piece_list[14], "W", "P", 2, 7)
PlacePiece(board_state.piece_list[15], "W", "P", 2, 8)
PlacePiece(board_state.piece_list[16], "B", "P", 7, 1)
PlacePiece(board_state.piece_list[17], "B", "P", 7, 2)
PlacePiece(board_state.piece_list[18], "B", "P", 7, 3)
PlacePiece(board_state.piece_list[19], "B", "P", 7, 4)
PlacePiece(board_state.piece_list[20], "B", "P", 7, 5)
PlacePiece(board_state.piece_list[21], "B", "P", 7, 6)
PlacePiece(board_state.piece_list[22], "B", "P", 7, 7)
PlacePiece(board_state.piece_list[23], "B", "P", 7, 8)
PlacePiece(board_state.piece_list[24], "B", "R", 8, 1)
PlacePiece(board_state.piece_list[25], "B", "N", 8, 2)
PlacePiece(board_state.piece_list[26], "B", "B", 8, 3)
PlacePiece(board_state.piece_list[27], "B", "Q", 8, 4)
PlacePiece(board_state.piece_list[28], "B", "K", 8, 5)
PlacePiece(board_state.piece_list[29], "B", "B", 8, 6)
PlacePiece(board_state.piece_list[30], "B", "N", 8, 7)
PlacePiece(board_state.piece_list[31], "B", "R", 8, 8)
board_state.player_turn = "W"



#setup board
#prompt user to select piece (provide list of pieces)
#prompt user to move piece (provide list of legal moves)


#prompt user to select piece (provide list of pieces)
#function takes a board state as a parameter
def UserSelection(state):
  selectables = []
  turn = state.player_turn
  for i in range(0, len(state.piece_list)):
    if state.piece_list[i].p_color == turn:
      selectables.append(state.piece_list[i])
  for i in range(0, len(selectables)):
    print selectables[i].p_type, selectables[i].p_rank, selectables[i].p_file
  selection_input = raw_input("Input coordinates (rank file): ")
  selection_rank = int(selection_input[0])
  selection_file = int(selection_input[2])
  for i in range(0, len(selectables)):
    if (selectables[i].p_rank == selection_rank and
      selectables[i].p_file == selection_file):
      return selectables[i]



#receives a board state and a piece as parameters
#returns list of coordinates, which are on the board, which a piece could
#move to if there were no barriers (other pieces)
def PathCoordinates(state, piece):
  path_list = []
  #pawn paths
  if piece.p_type == "P":
    #white pawn
    if piece.p_color == "W":
      if piece.p_rank + 1 <= 8:
        path_list.append([piece.p_rank + 1, piece.p_file])
        if piece.p_file + 1 <= 8:
          path_list.append([piece.p_rank + 1, piece.p_file + 1])
        if piece.p_file - 1 >= 1:
          path_list.append([piece.p_rank + 1, piece.p_file - 1])
      if piece.p_rank == 2:
        path_list.append([4, piece.p_file])
      return path_list
    #black pawn
    else:
      if piece.p_rank - 1 >= 1:
        path_list.append([piece.p_rank - 1, piece.p_file])
        if piece.p_file + 1 <= 8:
          path_list.append([piece.p_rank - 1, piece.p_file + 1])
        if piece.p_file - 1 >= 1:
          path_list.append([piece.p_rank - 1, piece.p_file - 1])
      if piece.p_rank == 7:
        path_list.append([5, piece.p_file])
      return path_list
  #knight paths
  elif piece.p_type == "N":
    temp_list = []
    temp_list.append([piece.p_rank + 2, piece.p_file - 1])
    temp_list.append([piece.p_rank + 2, piece.p_file + 1])
    temp_list.append([piece.p_rank + 1, piece.p_file - 2])
    temp_list.append([piece.p_rank + 1, piece.p_file + 2])
    temp_list.append([piece.p_rank - 1, piece.p_file - 2])
    temp_list.append([piece.p_rank - 1, piece.p_file + 2])
    temp_list.append([piece.p_rank - 2, piece.p_file - 1])
    temp_list.append([piece.p_rank - 2, piece.p_file + 1])
    for i in range(8):
      if (temp_list[i][0] >= 1 and temp_list[i][0] <= 8 and
        temp_list[i][1] >= 1 and temp_list[i][1] <= 8):
        path_list.append(temp_list[i])
    return path_list
  #bishop paths
  elif piece.p_type == "B":
    for i in range(1, 8):
      if piece.p_rank + i <= 8 and piece.p_file + i <= 8:
        path_list.append([piece.p_rank + i, piece.p_file + i])
      else:
        break
    for i in range(1, 8):
      if piece.p_rank - i >= 1 and piece.p_file + i <= 8:
        path_list.append([piece.p_rank - i, piece.p_file + i])
      else:
        break
    for i in range(1, 8):
      if piece.p_rank - i >= 1 and piece.p_file - i >= 1:
        path_list.append([piece.p_rank - i, piece.p_file - i])
      else:
        break
    for i in range(1, 8):
      if piece.p_rank + i <= 8 and piece.p_file - i >= 1:
        path_list.append([piece.p_rank + i, piece.p_file - i])
      else:
        break
    return path_list
  #rook paths
  elif piece.p_type == "R":
    horz_path = [1, 2, 3, 4, 5, 6, 7, 8]
    vert_path = [1, 2, 3, 4, 5, 6, 7, 8]
    del horz_path[(piece.p_file - 1)]
    del vert_path[(piece.p_rank - 1)]
    horz_coord_list = []
    vert_coord_list = []
    for i in range(7):
      horz_coord_list.append([piece.p_rank, horz_path[i]])
      vert_coord_list.append([vert_path[i], piece.p_file])
    path_list = horz_coord_list + vert_coord_list
    return path_list
  #queen paths
  elif piece.p_type == "Q":
    horz_path = [1, 2, 3, 4, 5, 6, 7, 8]
    vert_path = [1, 2, 3, 4, 5, 6, 7, 8]
    del horz_path[(piece.p_file - 1)]
    del vert_path[(piece.p_rank - 1)]
    horz_coord_list = []
    vert_coord_list = []
    for i in range(7):
      horz_coord_list.append([piece.p_rank, horz_path[i]])
      vert_coord_list.append([vert_path[i], piece.p_file])
    path_list = horz_coord_list + vert_coord_list
    for i in range(1, 8):
      if piece.p_rank + i <= 8 and piece.p_file + i <= 8:
        path_list.append([piece.p_rank + i, piece.p_file + i])
      else:
        break
    for i in range(1, 8):
      if piece.p_rank - i >= 1 and piece.p_file + i <= 8:
        path_list.append([piece.p_rank - i, piece.p_file + i])
      else:
        break
    for i in range(1, 8):
      if piece.p_rank - i >= 1 and piece.p_file - i >= 1:
        path_list.append([piece.p_rank - i, piece.p_file - i])
      else:
        break
    for i in range(1, 8):
      if piece.p_rank + i <= 8 and piece.p_file - i >= 1:
        path_list.append([piece.p_rank + i, piece.p_file - i])
      else:
        break
    return path_list
  #king paths
  else:
    if piece.p_rank + 1 <= 8:
      path_list.append([piece.p_rank + 1, piece.p_file])
    if piece.p_rank - 1 >= 1:
      path_list.append([piece.p_rank - 1, piece.p_file])
    if piece.p_file + 1 <= 8:
      path_list.append([piece.p_rank, piece.p_file + 1])
    if piece.p_file - 1 >= 1:
      path_list.append([piece.p_rank, piece.p_file - 1])
    if piece.p_rank + 1 <= 8 and piece.p_file + 1 <= 8:
      path_list.append([piece.p_rank + 1, piece.p_file + 1])
    if piece.p_rank - 1 >= 1 and piece.p_file + 1 <= 8:
      path_list.append([piece.p_rank - 1, piece.p_file + 1])
    if piece.p_rank - 1 >= 1 and piece.p_file - 1 >= 1:
      path_list.append([piece.p_rank - 1, piece.p_file - 1])
    if piece.p_rank + 1 <= 8 and piece.p_file - 1 >= 1:
      path_list.append([piece.p_rank + 1, piece.p_file - 1])
    return path_list

#receives a board state and a piece as parameters
def MoveSelection(state, piece):
  #legal pawn moves
  if piece.p_type == "P":
    print "wtf"
  #legal knight moves
  elif piece.p_type == "N":
    print "wtf"
  #legal bishop moves
  elif piece.p_type == "B":
    print "wtf"
  #legal rook moves
  elif piece.p_type == "R":
    print "wtf"
  #legal queen moves
  elif piece.p_type == "Q":
    print "wtf"
  #legal king moves
  else:
    print "wtf"    

print PathCoordinates(board_state, UserSelection(board_state))