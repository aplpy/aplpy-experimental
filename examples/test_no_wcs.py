import numpy as np
import matplotlib.pyplot as plt

from aplpy2.wcs_axes import WCSAxes

# Create plot and axes
fig = plt.figure()

# Initialize axes
ax = WCSAxes(fig, [0.1, 0.1, 0.8, 0.8])


ax.set_xspacing(10)
ax.set_yspacing(10)

# Show image
ax.imshow(np.random.random((128, 128)))

# Save to file
fig.savefig('identity.png', bbox_inches='tight')
