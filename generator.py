import numpy as np
import matplotlib.pyplot as plt
import parser as ps
import time
import seaborn as sns
import b2plot as bp
plt.style.use('belle2')

def linearFunction(x, a=0, b=0):
  return a*x + b
def expFunction(x, a=0, b=0):
  return a*np.exp(-b*x)
def gaussian(x, amplitude, sigma, mean):
  return amplitude*np.exp(-np.power(x - mean, 2.) / 
    (2 * np.power(sigma, 2.)))

def Generate(filename=None, delay=None, draw=False, save=None):
    if filename == '' or filename == 'None' or filename is None:
        raise Exception("Filename is wrong")
    else:
      sts = ps.Settings(filename)

    if delay is None:
      delay = 1

    histogram = None
    bins_list = []
    counts_list = []

    plt.figure(num=None, figsize=(12, 8), dpi=80, facecolor='w', edgecolor='b')
    plt.xlim(sts.emin, sts.emax)

    x = np.linspace(sts.emin, sts.emax, sts.nbins)
    y = linearFunction(x, sts.bkg_a, sts.bkg_b)
    temp_y = y + np.random.randn(sts.nbins)*50

    y = [i if i > 0 else i*0 for i in temp_y]
    counts, bins = np.histogram(x, weights=y, bins=int(sts.nbins), range=(sts.emin, sts.emax))
    if histogram is None:
        histogram = counts, bins
    else:
        histogram = histogram[0] + counts, bins

    bins_list.append(bins[:-1])
    counts_list.append(counts)

    if draw:
        bp.stacked(bins_list, weights=counts_list, bins=int(sts.nbins), range=(sts.emin, sts.emax))
        plt.pause(delay)

    x = np.linspace(sts.emin, sts.emax, sts.nbins)
    y = expFunction(x, sts.bkg_exp1, sts.bkg_exp2)
    counts, bins = np.histogram(x, weights=y, bins=int(sts.nbins), range=(sts.emin, sts.emax))
    if histogram is None:
        histogram = counts, bins
    else:
        histogram = histogram[0] + counts, bins
    bins_list.append(bins[:-1])
    counts_list.append(counts)

    if draw:
        bp.stacked(bins_list, weights=counts_list, bins=int(sts.nbins), range=(sts.emin, sts.emax))
        plt.pause(delay)

    for line in sts.lines:
        x = np.linspace(sts.emin, sts.emax, sts.nbins)
        y = gaussian(x, line.intensity, line.sigma, line.energy)
        counts, bins = np.histogram(x, weights=y, bins=int(sts.nbins), range=(sts.emin, sts.emax))
        if histogram is None:
            histogram = counts, bins
        else:
            histogram = histogram[0] + counts, bins
        bins_list.append(bins[:-1])
        counts_list.append(counts)
        if draw:
            bp.stacked(bins_list, weights=counts_list, bins=int(sts.nbins), range=(sts.emin, sts.emax))
            plt.pause(delay)

    if save is not None:
        plt.savefig(save)
    if draw:
        plt.show()
    else:
        return histogram