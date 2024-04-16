cake_width = int(input())
cake_length = int(input())

pieces_over = False

area_cake = cake_width * cake_length # 100 cm area
area_piece = 1*1 # 1 cm area
all_pieces = area_cake / area_piece
not_enough_pieces = 0
left_pieces = 0

command = input()
while command != "STOP":
    number_pieces = int(command)
    if all_pieces < number_pieces:
        not_enough_pieces = int(number_pieces - all_pieces)
        pieces_over = True
        break
    all_pieces -= number_pieces
    left_pieces = int(all_pieces)
    command = input()

if not pieces_over:
    print(f"{left_pieces} pieces are left.")
else:
    print(f"No more cake left! You need {not_enough_pieces} pieces more.")