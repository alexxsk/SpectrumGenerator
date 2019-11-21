from probfit import gen_toy, gaussian, exponential, linear, AddPdfNorm, \
                    Normalized, describe
import matplotlib.pyplot as plt
bound = (0, 10)
signalpdf = Normalized(gaussian, bound)
bgpdf1 = Normalized(linear, bound)
bgpdf2 = Normalized(exponential, bound)

total_pdf = AddPdfNorm(signalpdf, bgpdf1, bgpdf2)
params = {'mean' : 5, 'sigma' : 0.2,
          'm' : 20, 'c': 1, 'lambda' : 0.4, 
          'f_0' : 0.1 ,'f_1' : 0.2}                                                                                                            

toy = gen_toy(total_pdf, 100000, (0,10), **params, quiet=True)
plt.hist(toy, bins=150)
plt.show()
#toy = gen_toy(total_pdf, 1000, (1.83,1.91), mass=1.87, gamma=0.01, c=1.045, m=-0.43, f_0=0.5, quiet=False)

