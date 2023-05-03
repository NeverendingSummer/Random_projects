# import re
# import matplotlib.pyplot as plt
# import numpy as np
import os
from datetime import datetime
import os
now = datetime.now()
e = datetime.now()
# plt.style.use('seaborn-whitegrid')
# time = []
# date = []
# with open('20-45-22 01_05 100b.txt', 'r') as f:
#     pass
path = os.path.abspath(os.path.join(__file__, os.path.pardir))
print(os.path.abspath(os.path.join(__file__, os.path.pardir)))
current_time2 = now.strftime("%H-%M-%S")
open(f'{path}/logs/{now.strftime("%H-%M-%S")} {now.day}-{now.month}-{now.year} 100b.txt', 'w')
import datetime


print ("Current date and time = %s" % e)

print ("Today's date:  = %s/%s/%s" % (e.day, e.month, e.year))

print ("The time is now: = %s:%s:%s" % (e.hour, e.minute, e.second))