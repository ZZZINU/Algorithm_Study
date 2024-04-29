# 21942번: 부품 대여장
from collections import defaultdict
from datetime import datetime, timedelta
import sys

input = sys.stdin.readline

N, L, F = map(str, input().split())
N = int(N)
F = int(F)
maximum = timedelta(days=int(L[:3]), hours=int(L[4:6]), minutes=int(L[7:]))
minute = timedelta(minutes=1)

info = defaultdict(dict)

for i in range(int(N)):
    date, time, part, name = map(str, input().split())
    total_date = datetime.strptime(date + ' ' + time, '%Y-%m-%d %H:%M')
    part_info = {'date': total_date}

    if part in info[name]:
        info[name][part].append(part_info)
    else:
        info[name][part] = [part_info]

fines = defaultdict(int)

for name, parts in info.items():
    if not fines.get(name):
        fines[name] = 0

    for part, part_info_list in parts.items():
        for i in range(0, len(part_info_list), 2):
            first_date = part_info_list[i]['date']
            second_date = part_info_list[i+1]['date']

            duration = second_date - first_date

            if duration > maximum:
                fines[name] += ((duration - maximum) // minute) * F



has_fine = False
fines = sorted(fines.items())
for name, fine in fines:
    if fine is not 0:
        print(name, fine)
        has_fine = True

if not has_fine:
    print(-1)