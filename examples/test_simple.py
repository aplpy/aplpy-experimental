from astropy.io import fits

import matplotlib.pyplot as plt

from aplpy2.angle import Angle
from aplpy2.wcs_axes import WCSAxes

# Create plot and axes
fig = plt.figure()

# Initialize axes
ax = WCSAxes(fig, [0.1, 0.1, 0.8, 0.8], 'MSX_E.fits')

# Set tick spacing since no automatic method yet
ax.set_xspacing(Angle(0.2))
ax.set_yspacing(Angle(0.2, latitude=True))

# Show image
ax.imshow(fits.getdata('MSX_E.fits'), origin='lower', cmap=plt.cm.binary, interpolation='nearest', vmax=0.0001)

# Save to file
fig.savefig('test.png', bbox_inches='tight')
