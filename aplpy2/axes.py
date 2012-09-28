from matplotlib.axes import Axes
from matplotlib.ticker import NullFormatter
from matplotlib.transforms import Affine2D

from .locator import TransformLocator
from .formatter import TransformFormatter

IDENTITY = Affine2D()

class ParasiteAxes(Axes):

    def __init__(self, fig, rect, parent, transform=IDENTITY, xcoord_type='scalar', ycoord_type='scalar'):

        self.fig = fig
        self.rect = rect
        self._parent = parent

        Axes.__init__(self, fig, rect)

        self.xaxis.set_ticks_position('top')
        self.yaxis.set_ticks_position('right')
        self.set_frame_on(False)

        self.set_transform(transform=transform, xcoord_type=xcoord_type, ycoord_type=ycoord_type)

        self.xaxis.set_major_formatter(NullFormatter())
        self.yaxis.set_major_formatter(NullFormatter())

        fig.add_axes(self)

    def set_transform(self, transform=IDENTITY, xcoord_type='scalar', ycoord_type='scalar'):

        self.transform = transform

        self.major_loc_x = TransformLocator(coord='x', location='top', transform=transform, coord_type=xcoord_type)
        self.major_loc_y = TransformLocator(coord='y', location='right', transform=transform, coord_type=ycoord_type)
        self.xaxis.set_major_locator(self.major_loc_x)
        self.yaxis.set_major_locator(self.major_loc_y)

        self.xaxis.set_major_formatter(NullFormatter())
        self.yaxis.set_major_formatter(NullFormatter())

    def draw(self, renderer):

        self.axes.viewLim.set(self._parent.viewLim)
        self.set_position(self._parent.get_position())

        Axes.draw(self, renderer)


class HostAxes(Axes):

    def __init__(self, fig, rect, transform=IDENTITY, xcoord_type='scalar', ycoord_type='scalar', parent=None):

        self.fig = fig
        self.rect = rect
        self._parent = parent

        Axes.__init__(self, fig, rect)

        self.xaxis.set_ticks_position('bottom')
        self.yaxis.set_ticks_position('left')

        fig.add_axes(self)

        self.twin = ParasiteAxes(fig, rect, self)

        self.other = {}

        self.set_transform(transform=transform, xcoord_type=xcoord_type, ycoord_type=ycoord_type)

    def set_transform(self, transform=IDENTITY, xcoord_type='scalar', ycoord_type='scalar'):

        self.transform = transform

        self.major_loc_x = TransformLocator(coord='x', location='bottom', transform=transform, coord_type=xcoord_type)
        self.major_loc_y = TransformLocator(coord='y', location='left', transform=transform, coord_type=ycoord_type)
        self.xaxis.set_major_locator(self.major_loc_x)
        self.yaxis.set_major_locator(self.major_loc_y)

        self.major_form_x = TransformFormatter(locator=self.major_loc_x)
        self.major_form_y = TransformFormatter(locator=self.major_loc_y)
        self.xaxis.set_major_formatter(self.major_form_x)
        self.yaxis.set_major_formatter(self.major_form_y)

        self.twin.set_transform(transform=transform, xcoord_type=xcoord_type, ycoord_type=ycoord_type)

    def add_system(self, name, extra_transform):
        self.other[name] = HostAxes(self.fig, self.rect, self.transform + extra_transform, parent=self)
        self.other[name].patch.set_visible(False)
        self.other[name].set_frame_on(False)

    def set_xspacing(self, spacing):
        self.major_loc_x.spacing = spacing
        self.twin.major_loc_x.spacing = spacing

    def set_yspacing(self, spacing):
        self.major_loc_y.spacing = spacing
        self.twin.major_loc_y.spacing = spacing

    def draw(self, renderer):

        if self._parent is not None:
            self.axes.viewLim.set(self._parent.viewLim)
            self.set_position(self._parent.get_position())

        Axes.draw(self, renderer)
