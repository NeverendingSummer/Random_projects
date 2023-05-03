import subprocess
from datetime import datetime
import os
now = datetime.now()

process = subprocess.Popen(["ping", "ya.ru", "-t", "-l", "100"], stdout=subprocess.PIPE)
path = os.path.abspath(os.path.join(__file__, os.path.pardir))
open(f'{path}/logs/{now.strftime("%H-%M-%S")} {now.day}-{now.month}-{now.year} 100b.txt', 'w')
# синхронный busy spin, работа с потоком вывода, пока процесс не отработает
with open(f'{path}/logs/{now.strftime("%H-%M-%S")} {now.day}-{now.month}-{now.year} 100b.txt', 'a') as f:
    while True:
        now2 = datetime.now()
        current_time = now2.strftime("%H:%M:%S")
        output = process.stdout.readline()
        if output == b'' and process.poll() is not None:
            break
        if output:

            f.write(output.strip().decode('cp866') + " " + current_time + '\n')
            print(output.strip().decode('cp866') + " " + current_time)

# когда процесс завершится, poll() вернет код завершения, а не None
rc = process.poll()
#1519867