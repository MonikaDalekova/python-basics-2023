import math
count_competitions = int(input())
first_points = int(input())

points_gained = 0
wins = 0

for _ in range (0, count_competitions):
    competition = input()
    if competition == "W":
        points_gained += 2000
        wins += 1
    elif competition == "F":
        points_gained += 1200
    elif competition == "SF":
        points_gained += 720

total_points = points_gained + first_points
avg_points = points_gained / count_competitions
percent_wins = wins / count_competitions * 100

print(f"Final points: {total_points}")
print(f"Average points: {math.floor(avg_points)}")
print(f"{percent_wins:.2f}%")