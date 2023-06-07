import sys

_, person = map(int, sys.stdin.readline().split())

person_list = [person, 0, 0, 0, 0]

for i in range(2):
    off, on = map(int, sys.stdin.readline().split())
    person -= off
    person_list[2 * i + 1] = person
    person += on
    person_list[2 * i + 2] = person

print(max(person_list))
