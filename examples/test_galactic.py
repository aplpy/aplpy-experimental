from astropy.io import fits

import matplotlib.pyplot as plt

from aplpy2.angle import Angle
from aplpy2.wcs_axes import WCSAxes
from aplpy2.transforms.galactic import Galactic2EquatorialTransform

# Create plot and axes
fig = plt.figure()

# Initialize axes
ax1 = WCSAxes(fig, [0.1, 0.1, 0.3, 0.8], 'MSX_E.fits')

# Set tick spacing since no automatic method yet
ax1.set_xspacing(0.2)
ax1.set_yspacing(0.2)

# Show image
ax1.imshow(fits.getdata('MSX_E.fits'), origin='lower', cmap=plt.cm.binary, interpolation='nearest', vmax=0.0001)

# Initialize axes
ax2 = WCSAxes(fig, [0.6, 0.1, 0.3, 0.8], 'MSX_E.fits')

# Set tick spacing since no automatic method yet

ax2.set_transform(ax1.transform + Galactic2EquatorialTransform(), xcoord_type='longitude', ycoord_type='latitude')

ax2.set_xspacing(0.1)
ax2.set_yspacing(0.1)

# Show image
ax2.imshow(fits.getdata('MSX_E.fits'), origin='lower', cmap=plt.cm.binary, interpolation='nearest', vmax=0.0001)

# Save to file
fig.savefig('galactic.png', bbox_inches='tight')

