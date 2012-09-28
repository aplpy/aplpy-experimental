from astropy.io import fits
from astropy.wcs import WCS

from .axes import HostAxes
from .transforms.wcs import WcsPixel2WorldTransform

class WCSAxes(HostAxes):

    def __init__(self, fig, rect, input):

        if isinstance(input, basestring) and input.lower().endswith('.fits'):

            # Read in image
            hdu = fits.open(input)[0]

            # Set up WCS transformation
            wcs = WCS(hdu.header)
            wcs_trans = WcsPixel2WorldTransform(wcs)

            # Initalize axes
            HostAxes.__init__(self, fig, rect, wcs_trans, xcoord_type='longitude', ycoord_type='latitude')

        elif isinstance(input, WCS):

            # Set up WCS transformation
            wcs_trans = WcsPixel2WorldTransform(input)

            # Initalize axes
            HostAxes.__init__(self, fig, rect, wcs_trans, xcoord_type='longitude', ycoord_type='latitude')

        else:

            raise Exception("invalid type")
