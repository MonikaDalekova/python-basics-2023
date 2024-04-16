# start_num = int(input())
# final_num = int(input())
#
# for first in range(start_num, final_num + 1):
#     for second in range(start_num, final_num + 1):
#         for third in range(start_num, final_num + 1):
#             for fourth in range(start_num, final_num + 1):
#                 if first > fourth:
#                     if (second + third) % 2 == 0:
#                         if first % 2 == 0 and fourth % 2 != 0 or first % 2 != 0 and fourth % 2 == 0:
#                             print(f"{first}{second}{third}{fourth} ", end="")

start_num = int(input())
final_num = int(input())
for first in range(start_num, final_num + 1):
    for second in range(start_num, final_num + 1):
        for third in range(start_num, final_num + 1):
            for fourth in range(start_num, final_num + 1):
                is_special = False
                if first > fourth:
                    if (second + third) % 2 == 0:
                        if first % 2 == 0 and fourth % 2 != 0 or first % 2 != 0 and fourth % 2 == 0:
                            is_special = True
                if is_special:
                    print(f"{first}{second}{third}{fourth} ", end="")

