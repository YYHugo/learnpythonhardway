
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties as fntprop
import numpy as np
import csv
import sys

import decimal
import random

delimiter_char = '\t';

# upper_stop_band_wss_min=196.2e12 # Hz
# upper_stop_band_wss_max=197.3e12 # Hz
# lower_stop_band_wss_min=190.7e12 # Hz
# lower_stop_band_wss_max=191.25e12 # Hz

# use this frequency window
freq_window_min_wss=191.325e12 # Hz
freq_window_max_wss=196.150e12 # Hz

speed_light = 299792458 # meters per sec

wavelength_min = speed_light / freq_window_max_wss;
wavelength_max = speed_light / freq_window_min_wss;

colorlist=['b', 'g', 'r', 'c', 'm', 'y', 'k'];

for arg in sys.argv[1:]:
	np_read = np.genfromtxt(arg, delimiter=delimiter_char, skip_header=0);
	x = np_read[:, 0];
	y = np_read[:, 1];
	fontP = FontProperties()
  	fontP.set_size('small')
	plt.plot(x, y, color=random.choice(colorlist));
	legend([plot1], "title", prop = fontP)

plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.show()