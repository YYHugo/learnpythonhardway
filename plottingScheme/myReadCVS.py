# import csv
# import sys
# import numpy as np
# 
# arguments = sys.argv;
# filename = arguments[1];
# 
# with open(filename, 'rb') as f:
#     reader = csv.reader(f)
# 
#     try:
# 
#     except csv.Error as e:
#         sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))

import matplotlib.pyplot as plt
import csv
import sys
from StringIO import StringIO

arguments = sys.argv;
csv_file = arguments[1];

#f = csv.reader(open(csv_file))

#channel, osa, port1, error1, port2, error2, port3, error3, port4, error4 = zip(*f.items());

#plt.plot(channel[1:(len(osa)-1)], osa[1:(len(osa)-1)], 'r--');
#plt.xlabel("Channel");
#plt.ylabel("OSA");
#plt.axis(channel[1], channel[(len(channel)-1)], 0, osa[(len(osa)-1)]);
#plt.show();

import numpy as np

D_channel = np.genfromtxt(
    csv_file,               # file name
    skip_header=0,          # lines to skip at the top
    skip_footer=0,          # lines to skip at the bottom
    delimiter=' ',          # column delimiter
    dtype='int',            # data type
#    filling_values=0,       # fill missing values with 0
    usecols = (0),          # columns to read
    names=True)        # column names

D_osa = np.genfromtxt(
    csv_file,               # file name
    skip_header=0,          # lines to skip at the top
    skip_footer=0,          # lines to skip at the bottom
    delimiter=' ',          # column delimiter
    dtype='float',          # data type
#    filling_values=0,       # fill missing values with 0
    usecols = (1),          # columns to read
    names=True)            # column names

D_port1 = np.genfromtxt(
    csv_file,               # file name
    skip_header=0,          # lines to skip at the top
    skip_footer=0,          # lines to skip at the bottom
    delimiter=' ',          # column delimiter
    dtype='float',          # data type
#    filling_values=0,       # fill missing values with 0
    usecols = (2),          # columns to read
    names=True)          # column names

D_error1 = np.genfromtxt(
    csv_file,               # file name
    skip_header=0,          # lines to skip at the top
    skip_footer=0,          # lines to skip at the bottom
    delimiter=' ',          # column delimiter
    dtype='float',          # data type
#    filling_values=0,       # fill missing values with 0
    usecols = (3),          # columns to read
    names=True)          # column names

D_port2 = np.genfromtxt(
    csv_file,               # file name
    skip_header=0,          # lines to skip at the top
    skip_footer=0,          # lines to skip at the bottom
    delimiter=' ',          # column delimiter
    dtype='float',          # data type
#    filling_values=0,       # fill missing values with 0
    usecols = (4),          # columns to read
    names=True)          # column names

D_error2 = np.genfromtxt(
    csv_file,               # file name
    skip_header=0,          # lines to skip at the top
    skip_footer=0,          # lines to skip at the bottom
    delimiter=' ',          # column delimiter
    dtype='float',          # data type
#    filling_values=0,       # fill missing values with 0
    usecols = (5),          # columns to read
    names=True)          # column names

D_port3 = np.genfromtxt(
    csv_file,               # file name
    skip_header=0,          # lines to skip at the top
    skip_footer=0,          # lines to skip at the bottom
    delimiter=' ',          # column delimiter
    dtype='float',          # data type
#    filling_values=0,       # fill missing values with 0
    usecols = (6),          # columns to read
    names=True)          # column names

D_error3 = np.genfromtxt(
    csv_file,               # file name
    skip_header=0,          # lines to skip at the top
    skip_footer=0,          # lines to skip at the bottom
    delimiter=' ',          # column delimiter
    dtype='float',          # data type
#    filling_values=0,       # fill missing values with 0
    usecols = (7),          # columns to read
    names=True)          # column names

D_port4 = np.genfromtxt(
    csv_file,               # file name
    skip_header=0,          # lines to skip at the top
    skip_footer=0,          # lines to skip at the bottom
    delimiter=' ',          # column delimiter
    dtype='float',          # data type
#    filling_values=0,       # fill missing values with 0
    usecols = (8),          # columns to read
    names=True)          # column names

D_error4 = np.genfromtxt(
    csv_file,               # file name
    skip_header=0,          # lines to skip at the top
    skip_footer=0,          # lines to skip at the bottom
    delimiter=' ',          # column delimiter
    dtype='float',          # data type
#    filling_values=0,       # fill missing values with 0
    usecols = (9),          # columns to read
    names=True)          # column names
line = 0;
print type(D_channel[4]);
print D_osa;
# for line in range[0:len(D_channel)-1]:
#for line in D_channel:
#    print "{0} \t {1} \t {2} \t {3} \t {4} \t {5} \t {6} \t {7} \t {8} \t {9}".format(str(D_channel[line]), str(D_osa[line]), str(D_port1[line]), str(D_error1[line]), str(D_port2[line]), str(D_error2[line]), str(D_port3[line]), str(D_error3[line]), str(D_port4[line]), str(D_error4[line]))
