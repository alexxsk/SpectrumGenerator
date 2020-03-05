"""
Example with the spectrum generator based on creating response function and than toy monte carlo. 

"""
from probfit import gen_toy, gaussian, exponential, linear, AddPdfNorm, \
                    Normalized, describe
import matplotlib.pyplot as plt

# There are pdf's with background and signal
bound = (0, 10)
signalpdf = Normalized(gaussian, bound)
bgpdf1 = Normalized(linear, bound)
bgpdf2 = Normalized(exponential, bound)

# Total pdf's create and parameters for generating 
total_pdf = AddPdfNorm(signalpdf, bgpdf1, bgpdf2)
params = {'mean' : 5, 'sigma' : 0.2,
          'm' : 20, 'c': 1, 'lambda' : 0.4, 
          'f_0' : 0.1 ,'f_1' : 0.2}                                                                                                            

# Toy monte carlo generation
toy = gen_toy(total_pdf, 100000, (0,10), **params, quiet=True)

# Build histogram 
plt.hist(toy, bins=200)
plt.show()

