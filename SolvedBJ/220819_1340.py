import sys

day_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month = ['January', 'February', 'March', 'April', 'May', 'June',
         'July', 'August', 'September', 'October', 'November', 'December']

M, DD, YYYY, HHMM = sys.stdin.readline().strip().split()
DD = int(DD[:-1]) - 1
YYYY = int(YYYY)
HH, MM = map(int, HHMM.split(':'))

whole = 365 * 24 * 60
if (YYYY % 4 == 0) and (YYYY % 100 != 0) or (YYYY % 400 == 0):
    whole += 24 * 60
    day_in_month[1] += 1
M = sum(day_in_month[:month.index(M)])

days = M + DD
minutes = days * 24 * 60 + HH * 60 + MM
print(100 * minutes / whole)