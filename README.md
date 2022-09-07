## The software was made for the generation of different device spectrums for further analysis.

Functionality includes:

- GUI (Tkinter) where you can set spectrum characteristics like energy, intensity, FWHM (resolution), and background. It is also possible to set variables via the settings file (comments support included).
- File with the generated spectrum includes spectrum peaks (Gaussians) with given resolution and background simulation based on statistical scattering according to Poisson distribution if the number of events in the channel is less than 10, and Gaussian approximation if the number of events is greater then 10 (sigma = sqrt(N), where N is a counts number in a channel).
- Graphical interpretation of a spectrum also shows.
