import os
from io import StringIO  
import numpy as np
import matplotlib.pyplot as plt

PATH = "CE/data/"

#----------------- Y_ib -----------------#
# read file and store into c variable
with open(PATH + "gie.csv", "r") as f:
	gie=f.read()

# convert c into another suitable format
c = StringIO(gie)
# load c into x and y numpy arrays
f1, gie = np.loadtxt(c, delimiter=',', usecols=(0, 1), unpack=True)


with open(PATH + "bie.csv", "r") as f:
	bie=f.read()
c = StringIO(bie)
f2, bie = np.loadtxt(c, delimiter=',', usecols=(0, 1), unpack=True)


#----------------- Y_fb -----------------#
with open(PATH + "gfe.csv", "r") as f:
	gfe=f.read()
c = StringIO(gfe)
f3, gfe = np.loadtxt(c, delimiter=',', usecols=(0, 1), unpack=True)

with open(PATH + "-bfe.csv", "r") as f:
	bfe=f.read()
c = StringIO(bfe)
f4, bfe = np.loadtxt(c, delimiter=',', usecols=(0, 1), unpack=True)


#----------------- Y_ob -----------------#
with open(PATH + "goe.csv", "r") as f:
	goe=f.read()
c = StringIO(goe)
f5, goe = np.loadtxt(c, delimiter=',', usecols=(0, 1), unpack=True)

with open(PATH + "boe.csv", "r") as f:
	boe=f.read()
c = StringIO(boe)
f6, boe = np.loadtxt(c, delimiter=',', usecols=(0, 1), unpack=True)


#----------------- Y_rb -----------------#
with open(PATH + "-gre.csv", "r") as f:
	gre=f.read()
c = StringIO(gre)
f7, gre = np.loadtxt(c, delimiter=',', usecols=(0, 1), unpack=True)

with open(PATH + "-bre.csv", "r") as f:
	bre=f.read()
c = StringIO(bre)
f8, bre = np.loadtxt(c, delimiter=',', usecols=(0, 1), unpack=True)

#---------------------------------------#

def visualize_CE_plot():
	# plot it
	plt.figure(1,figsize=(10,8))

	plt.subplot(221)
	# plt.subplot(411)
	plt.gca().set_title("$y_{ie}$")
	plt.plot(f1, gie, label="$g_{ib}$")
	plt.plot(f2, bie, label="$b_{ib}$")
	plt.grid(True)
	plt.xscale('log')
	plt.legend()
	plt.ylabel("$mS$")


	plt.subplot(223)
	# plt.subplot(412)
	plt.gca().set_title("$y_{fe}$")
	plt.plot(f3, gfe, label="$g_{fe}$")
	plt.plot(f4, bfe, label="$-b_{fe}$")
	plt.grid(True)
	plt.xscale('log')
	plt.legend()
	plt.xlabel("$f\ (MHz)$")
	plt.ylabel("$mS$")


	plt.subplot(222)
	# plt.subplot(413)
	plt.gca().set_title("$y_{oe}$")
	plt.plot(f5, goe, label="$g_{oe}$")
	plt.plot(f6, boe, label="$b_{oe}$")
	plt.grid(True)
	plt.xscale('log')
	plt.legend()


	plt.subplot(224)
	# plt.subplot(414)
	plt.gca().set_title("$y_{re}$")
	plt.plot(f7, gre, label="$-g_{re}$")
	plt.plot(f8, bre, label="$-b_{re}$")
	plt.grid(True)
	plt.xscale('log')
	plt.legend()
	plt.xlabel("$f\ (MHz)$")

	plt.suptitle("2N4957 Common emitter (C.E.) Y parameters. $y = g + j\cdot b$")
	plt.show()


#visualize_CE_plot()
