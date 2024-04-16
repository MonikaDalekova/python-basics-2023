command = input()

word = ""
n_counter = 0
o_counter = 0
c_counter = 0
secret_command_trigger = False
while command != "End":
    is_it_letters = command.isalpha()
    if is_it_letters:
        if command != "n" and command != "o" and command != "c":
            word += command
        else:
            if command == "n":
                n_counter += 1
                if n_counter > 1:
                    word += command
            elif command == "o":
                o_counter += 1
                if o_counter > 1:
                    word += command
            elif command == "c":
                c_counter += 1
                if c_counter > 1:
                    word += command
            if n_counter >= 1 and o_counter >= 1 and c_counter >= 1:
                print(f"{word}", end=" ")
                word = ""
                n_counter = 0
                o_counter = 0
                c_counter = 0
    command = input()




