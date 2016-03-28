
from matplotlib import pyplot as plt
import numpy as np
import csv
import sys

import decimal

delimiter_char = '\t';

np_read = np.genfromtxt(sys.argv[1], delimiter=delimiter_char, skip_header=0);
x = np_read[:, 0];
y = np_read[:, 1];

plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.plot(x, y, 'r-')
plt.show()