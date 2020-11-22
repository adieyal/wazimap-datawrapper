import copy
from uuid import uuid4
import json

icon_template = {
    "id": "circle",
    "path": "M1000 350a500 500 0 0 0-500-500 500 500 0 0 0-500 500 500 500 0 0 0 500 500 500 500 0 0 0 500-500z",
    "horiz-adv-x": 1000,
    "scale": 1,
    "height": 700,
    "width": 1000
}

text_template = {
    "bold": False,
    "italic": False,
    "uppercase": False,
    "space": False,
    "color": "#333333",
    "fontSize": 14,
    "halo": "#f2f3f0"
}

template = {
    "id": "m8",
    "data": {
        "marker-color": "#7e7e7e",
        "marker-size": "medium",
        "marker-symbol": "",
        "name": ""
    },
    "wikidata": None,
    "type": "point",
    "title": "",
    "icon": icon_template,
    "scale": 1,
    "textPosition": None,
    "markerColor": "#ff0000",
    "markerSymbol": "",
    "markerTextColor": "#333333",
    "anchor": "bottom-center",
    "offsetY": 0,
    "offsetX": 0,
    "labelStyle": "plain",
    "text": text_template,
    "class": "",
    "rotate": 0,
    "visible": True,
    "locked": False,
    "preset": "-",
    "visibility": {
        "mobile": True,
        "desktop": True
    },
    "tooltip": {
        "enabled": False,
        "text": ""
    },
    "connectorLine": {
        "enabled": False,
        "arrowHead": "lines",
        "type": "curveRight",
        "targetPadding": 3,
        "stroke": 1,
        "lineLength": 0
    },
    "coordinates": [0, 0],
    "orgLatLng": [0, 0],
}

class PointMarker:

    SIZE_MEDIUM = "medium"

    def __init__(self, name, latitude, longitude):
        self._data = copy.deepcopy(template)
        self.coordinates = [longitude, latitude]
        self.name = name
        self.id = str(uuid4())

    @property
    def id(self):
        return self.data["id"]
        

    @id.setter
    def id(self, i):
        self.data["id"] = i

    @property
    def coordinates(self):
        return self.data["coordinates"]

    @coordinates.setter
    def coordinates(self, c):
        self.data["coordinates"] = c
        self.data["orgLatLng"] = c

    @property
    def marker_color(self):
        return self.data["marker-color"]

    @marker_color.setter
    def marker_color(self, c):
        self.data["data"]["marker-color"] = c
        self.data["markerColor"] = c

    @property
    def name(self):
        return self.data["title"]

    @name.setter
    def name(self, n):
        self.data["title"] = n
        self.data["data"]["name"] = n

    @property
    def color(self):
        return self.data["marker-color"]

    @color.setter
    def color(self, c):
        self.data["marker-color"] = c

    
    def set_size(self, size):
        self.data["marker-size"] = SIZE_MEDIUM

    @property
    def data(self):
        return self._data
