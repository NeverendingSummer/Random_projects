import re
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-whitegrid')
time = []
date = []
start_end = []
with open('20-15-21 02_05 100b.txt', 'r') as f:
    for i in f:
        try:
            time.append(i.split()[5])
            date.append(i.split()[7])
        except IndexError:
            time.append('время=100мс')

time_parsed = []
date_parsed = []
for i in range(len(time) - 1):
    time_parsed.append(time[1:][i][6:-2])
for i in range(len(date) - 1):
    date_parsed.append(date[1:][i])
print('here')

test = set(time_parsed)

try:
    test.remove('упн')
    test.remove('')
    test.remove('упна.15:24:')
except KeyError:
    pass

counter = []
uniq = []
for i in test:
    try:

        uniq.append(i)
    except ValueError:
        pass

for i in uniq:
    time_parsed = sorted(time_parsed)
    counter.append(time_parsed.count(i))

check = 0
print(counter)
for i in range(len(counter)):
    if counter[i] > 10000:
        counter[i] = round(counter[i] / 100)
print(counter)
print(uniq)

plt.figure(figsize=(20, 10), dpi=80)
plt.scatter(x=uniq, y=counter, color="green",
            marker="o", s=30, linewidths=1)

plt.text(-2, -100, fr'start-{date[1]} end-{date[-1]}', fontsize=15)

plt.show()
