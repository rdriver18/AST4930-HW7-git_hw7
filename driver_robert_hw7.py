import numpy as np
from astropy import units as u
import matplotlib.pyplot as plt

sed = np.loadtxt("./sed.txt" , skiprows=3, delimiter=",")# loading the sed.txt file into python

wavelength= sed[:,0] # spliting the columns to make it more usefull
sluminosity=sed[:,1]

n_wavelength=[]# creating new arrays for the 10-1000
n_sluminosity=[]
wavelength_range=np.where(wavelength >= 10) # only need to be greater than 10 because the highest is just under 1000
for i in range (len(wavelength_range[0])):
    n_wavelength.append(wavelength[i]) # appending the arrays to only be greater than 10 with its corresponding specific luminosities
    n_sluminosity.append(sluminosity[i])

wavelength_units=n_wavelength * u.micron
sluminosity_units=n_sluminosity*u.Lsun/u.micron #having units ready for conversion

integrated_sed=np.trapz(wavelength_units, sluminosity_units) # integrating 
integrated_changed_units=integrated_sed.to(u.erg/u.s) #converting the units to erg/s
print(integrated_sed)
print(integrated_changed_units)


w_sed_units=wavelength*u.micron 
sl_sed_units=sluminosity*u.Lsun/u.micron #adding units to the entire data from the sed.txt file

fig = plt.figure() # plotting the entire contents of the sed.txt file
ax=fig.add_subplot()
line, = ax.plot(w_sed_units, sl_sed_units)
ax.set_xscale('log')
ax.set_yscale('log')
plt.xlabel('Wavelength (microns)',color='g')
plt.ylabel('Specific Luminosity (Lsun/micron)', color='b')
plt.title('Spectral Energy Distribution')

plt.savefig('driver_robert_hw7.png',dpi=300) #saveing plot as a png.

print('The plot is in a png file')


