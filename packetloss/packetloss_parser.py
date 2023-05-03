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

# print(time[2:])
# print(date[1:])

# print(len(time[1:]))
# print(len(date[1:]))

time_parsed = []
date_parsed = []
for i in range(len(time) - 1):
    time_parsed.append(time[1:][i][6:-2])
for i in range(len(date) - 1):
    date_parsed.append(date[1:][i])
print('here')
# print(time_parsed[1:])
# print(date_parsed)
# print(type(time_parsed), type(time_parsed[0]))
# print(set(time_parsed))
test = set(time_parsed)
# print(test)
# print(test.remove('упна.15:24:'))
# print(test)
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
        # print(int(i))
        uniq.append(i)
    except ValueError:
        pass
# print(uniq)for i in uniq[1:-1]:
for i in uniq:
    time_parsed = sorted(time_parsed)
    counter.append(time_parsed.count(i))
# print('here')
# print(counter)
# print(time_parsed[0]+time_parsed[1])
# print(int(time_parsed[0])+int(time_parsed[1]))
# plt.pie(counter, labels=uniq, startangle=30)
# plt.show()
# print(uniq)
# print(len(uniq[1]), len(uniq[18]), len(uniq[2]), uniq[1], uniq[18], uniq[2])

check = 0
print(counter)
for i in range(len(counter)):
    if counter[i] > 10000:
        counter[i] = round(counter[i] / 100)
print(counter)
print(uniq)
# plotting a histogram
# plt.hist(counter, bins, range, color='green',
#          histtype='bar', rwidth=0.2)
plt.figure(figsize=(20, 10), dpi=80)
plt.scatter(x=uniq, y=counter, color="green",
            marker="o", s=30, linewidths=1)
# plt.text(100,100,fr'${date[1]}\ \{date[-1]}')
plt.text(-2, -100, fr'start-{date[1]} end-{date[-1]}', fontsize=15)
# function to show the plot
plt.show()
