actor_name = input()
academy_points = float(input())
count_judges = int(input())

total_points = academy_points
for _ in range(0, count_judges):
    name_judge = input()
    judge_points = float(input())
    sum_points_formula = len(name_judge) * judge_points / 2
    total_points += sum_points_formula
    diff = abs(total_points - 1250.5)
    if total_points > 1250.5:
        break

if total_points <= 1250.5:
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")
else:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")