import csv
import sys

delimiter_char = ';';

with open(sys.argv[1] , 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=delimiter_char)
    for column in reader:
        print column
