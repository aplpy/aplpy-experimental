from matplotlib.transforms import Affine2D

from astropy.io import fits
from astropy.wcs import WCS

from .axes import HostAxes
from .transforms.wcs import WcsPixel2WorldTransform

class WCSAxes(HostAxes):

    def __init__(self, fig, rect, input=None):

        HostAxes.__init__(self, fig, rect)

        self.set_input(input=input)

    def set_input(self, input=None):

        if isinstance(input, basestring) and input.lower().endswith('.fits'):

            # Read in image
            hdu = fits.open(input)[0]

            # Set up WCS transformation
            wcs = WCS(hdu.header)
            wcs_trans = WcsPixel2WorldTransform(wcs)

            # Initalize axes
            self.set_transform(wcs_trans, xcoord_type='longitude', ycoord_type='latitude')

        elif isinstance(input, WCS):

            # Set up WCS transformation
            wcs_trans = WcsPixel2WorldTransform(input)

            # Initalize axes
            self.set_transform(wcs_trans, xcoord_type='longitude', ycoord_type='latitude')

        elif input is None:

            # Set up identity transformation
            identity = Affine2D()

            # Initalize axes
            self.set_transform(identity, xcoord_type='scalar', ycoord_type='scalar')

        else:

            raise Exception("invalid type")
