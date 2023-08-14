import sys
import matplotlib


import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([10.25, 11.75, 11.25, 11, 11.25, 11.5, 11.15, 12.25, 10, 10.2, 10, 9.7 ])
ypoints = np.array(["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov","Dec"])

plt.plot(ypoints,xpoints, linestyle = 'solid')
plt.plot(ypoints, xpoints, color = 'orange')
plt.grid()

plt.xlabel("Months")
plt.ylabel("Wind Speed(Km/h)")
# plt.show()
plt.savefig('test_image.tiff')

