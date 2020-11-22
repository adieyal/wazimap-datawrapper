"""
Originally based on https://github.com/chekos/datawrapper but there have been substantial changes
"""

import datawrapper.datawrapper as dw
from IPython.display import HTML, Image
from .pointmarker import PointMarker
from .boundarymarker import BoundaryMarker
from .metadata import Metadata
from .pointbuilder import PointBuilder

Datawrapper = dw.Datawrapper
