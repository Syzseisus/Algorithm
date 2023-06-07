import sys

game, wins = map(int, sys.stdin.readline().split())
win_rate = (100 * wins) // game

if win_rate >= 99:
    print(-1)

else:
    lb = 1
    ub = game
    answer = 0
    while lb <= ub:
        mid = (lb + ub) // 2
        new_win_rate = (100 * (wins + mid)) // (game + mid)
        if new_win_rate <= win_rate:
            lb = mid + 1
        else:
            answer = mid
            ub = mid - 1

    print(answer)
