n = int(input())
current_sum = int(input()) + int(input())

diff_sum = 0

for _ in range(n - 1):
    next_sum = int(input()) + int(input())

    if abs(current_sum - next_sum) > diff_sum:
        diff_sum = abs(current_sum - next_sum)

    current_sum = next_sum

if diff_sum == 0:
    print(f"Yes, value={current_sum}")
else:
    print(f"No, maxdiff={diff_sum}")