from random import randrange

class OutRangeError(Exception):
    pass

class PositionUnavailableError(Exception):
    pass

# Tictactoe

winning_positions = sorted(['123','456','789','147','258','369','159','357'])
player_responses = ''
computer_responses = ''
board = []
position = 1
for r in range(3):
    row = []
    for c in range(3):
        row.append(position)
        position += 1
    board.append(row)

board[1][1] = 'x'
computer_responses += '5'
positions_free = 8

def draw_board(board):
    print(f"Posiciones disponibles: {positions_free}")
    for dr in range(len(board)):
        row = board[dr]
        print(f"""+-------+-------+-------+ \n| \t| \t| \t| \n|   {row[0]}   |   {row[1]}   |   {row[2]}   | \n| \t| \t| \t|""")
    print("+-------+-------+-------+")

def welcome():
    print("""
    Bienvenido a TIC-TAC-TOE
    Yo tiro primero!
    """)
    draw_board(board=board)
    print("Es tu turno!")

def validate_position(position):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == position:
                if board[row][col] != 'x' or board[row][col] != 'o':
                    return True
                else:
                    return False

def assign_position(position, player):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == position: 
                board[row][col] = player

def choice_a_random_num():
    return randrange(10)

def validate_board(player):
    if len(player_responses) >= 3 or len(computer_responses) >= 3:
        res = ""
        if player == 'o':
            if len(player_responses) >= 3:
                res = res.join(sorted(player_responses))
        else:
            if len(computer_responses) >= 3:
                res = res.join(sorted(computer_responses))
        for pos in winning_positions:
            counter = 0
            for num in res:
                if num in pos:
                    counter += 1
            if counter == 3:
                return True
    return False

# Starting the game...
welcome()
while positions_free > 0:
    try:
        num_by_user = int(input("Escribe el numero de la celda: "))
        if num_by_user not in range(1, 10):
            raise OutRangeError("Solo puedes elegir numeros del 1 al 9")
        
        if not validate_position(position=num_by_user):
            raise PositionUnavailableError('La posicion ya esta ocupada, elige otra celda!')

        assign_position(position=num_by_user, player='o')
        player_responses += str(num_by_user)
        positions_free -= 1
        draw_board(board=board)
        if validate_board('o'):
            print("Ganaste!")
            break

        print("Es mi turno...")
        positions_free -= 1
        computer = choice_a_random_num()
        while not validate_position(position=computer):
            computer = choice_a_random_num()

        assign_position(position=computer, player='x')
        computer_responses += str(computer)
        draw_board(board=board)
        if validate_board('x'):
            print("La computador gana")
            break
        

    except ValueError:
        print("ERROR -> Solo puedes elegir numeros, no letras!")
    except OutRangeError as e:
        print(f"ERROR -> {e}")
    except PositionUnavailableError as e:
        print(f"ERROR -> {e}")

if positions_free == 0:
    print("##################Tablas, se acabaron las posiciones!#####################")


