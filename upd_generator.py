"""  
Spectrum generator is a core of this program, it generates
different type of spectrum:
  1. Peaks with or without extention (with or without FWHM)
  2. Background spectrum that consist of exponential
     and linear parts with or without statistical deviations
  3. Total spectrum with or without statistical debiations

"""
import numpy as np
import matplotlib.pyplot as plt
import parser as ps
import time
import seaborn as sns
import b2plot as bp
from scipy.signal import unit_impulse

plt.style.use('belle2')

def non_minus(function):
    """
    Decorator is made spectrum without < 0 values

    """
    def decorator(*args, **kwargs):
        if function(*args, **kwargs) < 0:
            return 0
        else:
            return function(*args, **kwargs)
    return decorator

def linear_function(x, a=0, b=0):
    """
    First order poly function for backgroud
    
    @params:
        x(float) - Requiered: x for polynom
        a(float) - Requiered: First polynomial parameter
        b(float) - Requiered: Second polynomial parameter

    """
    return a*x + b

def exponential_function(x, a=0, b=0):
    """
    Exponential function for bkg

    @params:
        x(float) - Requiered: ...
        a(float) - Requiered: ...
        b(float) - Requiered: ...


    """
    return a*np.exp(-b*x)

@non_minus
def background_function(x, a, b, c, d):
    """
    Background function with decorated non-minus values
    function.

    @params:
        x(float) - Requiered: ...
        a(float) - Requiered: ...
        b(float) - Requiered: ...
        c(float) - Requiered: ...
        d(float) - Requiered: ...

    """
    return linear_function(x, a, b) + exponential_function(x, c, d)

def gaussian_function(x, amplitude, sigma, mean):
    """
    Gaussian function for peaks

    @params:
        x(float) - Requiered: ...
        amplitude(float) - Requiered: ...
        sigma(float) - Requiered: ...
        mean(float) - Requiered: ...

    """
    return amplitude*np.exp(-np.power(x - mean, 2.) / 
    (2 * np.power(sigma, 2.)))

@non_minus
def statistical_scatter(value):
    """
    Statistical spectrum scattering.
    If value less than 10 it will be scattered by poisson distr.
    If value greater than 10 it will be scattered by gauss appr. distr.
    
    @params:
        value(float) - Requiered: ...

    """
    if value < 10:
        return float(np.random.poisson(value, 1))
    else:
        return float(np.random.normal(value, np.sqrt(value),1))

class Generator(object): 
    def __init__(self, filename=None):
        """

        __init__
        @params:
            filename(str) - Requiered: Name of settings file

        """
        if filename == '' or filename == 'None' or filename is None:
            raise Exception("Filename is wrong")
        else:
            self.sts = ps.Settings(filename)

        self.x = np.linspace(self.sts.emin, self.sts.emax, 
                             self.sts.nbins)
        self.signals = [line.energy for line in self.sts.lines]
        #self.signals = {line.energy: line.intensity 
         #               for line in self.sts.lines}

    def generate_peaks_with_extension(self):
        """
        Method returns array with generated peaks only with 
        FWHM and statistical deviations

        @params:
            -

        """
        result = np.zeros(shape=self.sts.nbins)
        for line in self.sts.lines:
            result += gaussian_function(self.x, line.intensity,
                                        line.sigma, line.energy)
        return [statistical_scatter(i) for i in result]

    def generate_peaks_without_extension(self):
        """
        Method returns array with generated peaks only without
        FWHM and statistical deviations

        @params:
            -

        """
        pass

    def generate_bkg_without_stat(self):
        """
        Method returns array with exp+lin background only, without
        statistical deviations

        @params:
            -

        """
        return [background_function(x, self.sts.bkg_a, self.sts.bkg_b,
                                   self.sts.bkg_exp1, self.sts.bkg_exp2)
                for x in self.x]

    def generate_bkg_with_stat(self):
        """
        Method returns array with exp+lin background only, with 
        statistical deviations

        @params:
            -

        """
       return [statistical_scatter(x) 
                for x in self.generate_bkg_without_stat()]
         
    def generate_total_without_stat(self):
        """
        Method returns array with total spectrum with peaks with FWHM
        and lin+exp background without statistical deviations

        @params:
            -

        """
        result = np.zeros(shape=self.sts.nbins)
        result += self.generate_peaks_with_extension()
        result += self.generate_bkg_without_stat()
        return result

    def generate_total_with_stat(self):
        """
        Method returns array with total spectrum with peaks with FWHM
        and lin+exp background with statistical deviations

        @params:
            -

        """
        result = np.zeros(shape=self.sts.nbins)
        result += self.generate_peaks_with_extension()
        result += self.generate_bkg_with_stat()
        return result
                

generator = Generator("settings.txt")

print(len(generator.x), len(generator.generate_peaks_with_extension()))
bins = generator.x
weights = generator.generate_total_with_stat()
plt.hist(bins, weights=weights, bins=800)

plt.show()
