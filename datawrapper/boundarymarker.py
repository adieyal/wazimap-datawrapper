import copy
from uuid import uuid4

template = {
    "id": "",
    "data": {
        "admin_level": 8,
        "bbox": [
            19.6172099937714,
            -34.83417005583,
            20.8713899746728,
            -34.2036000668197
        ],
        "land_area": "administrative",
        "min_zoom": 5,
        "name": "",
        "name_de": "",
        "name_en": "",
        "osm_id": 79678,
        "parent_id": 79680,
        "label": "",
        "level": 1
    },
    "size": 3477.85,
    "type": "area",
    "title": "",
    "visible": True,
    "fill": True,
    "stroke": True,
    "exactShape": True,
    "highlight": True,
    "icon": {
        "id": "area",
        "path": "M225-132a33 33 0 0 0-10 1 38 38 0 0 0-27 28l-187 798a39 39 0 0 0 9 34 37 37 0 0 0 33 12l691-93 205 145a38 38 0 0 0 40 2 38 38 0 0 0 20-36l-54-653a38 38 0 0 0-17-28 38 38 0 0 0-32-5l-369 108-274-301a39 39 0 0 0-28-12z",
        "horiz-adv-x": 1000,
        "scale": 1.1,
        "outline": "2px"
    },
    "feature": {
        "type": "Feature",
        "properties": [],
        "geometry": {
            "type": "Polygon",
            "coordinates": []
        }
    },
    "visibility": {
        "mobile": True,
        "desktop": True
    }
}

class BoundaryMarker:
    def __init__(self, name):
        self._data = copy.deepcopy(template)
        self.name = name
        self.id = str(uuid4())
        self.properties = Properties()

    @property
    def id(self):
        return self.data["id"]
        

    @id.setter
    def id(self, i):
        self.data["id"] = i


    @property
    def name(self):
        return self.data["title"]

    @property
    def properties(self):
        return Properties(self.data["properties"])


    @properties.setter
    def properties(self, p):
        self.data["properties"] = p.data

    @name.setter
    def name(self, n):
        self.data["title"] = n
        self.data["data"]["name"] = n
        self.data["data"]["label"] = n


    @property
    def coordinates(self):
        return self.data["feature"]["geometry"]["coordinates"]

    @coordinates.setter
    def coordinates(self, c):
        self.data["feature"]["geometry"]["coordinates"] = c


    @property
    def data(self):
        return self._data



property_template = {
    'fill': '#ffffff',
    'fill-opacity': 0.01,
    'stroke': '#888',
    'stroke-width': 1,
    'stroke-opacity': 1,
    'stroke-dasharray': '1,1',
    'pattern': 'solid',
    'pattern-line-width': 2,
    'pattern-line-gap': 2
}

class Properties:
    def __init__(self, data=None):
        self._data = data or copy.deepcopy(property_template)

    @property
    def fill(self):
        return self.data["fill"]

    @fill.setter
    def fill(self, f):
        self.data["fill"] = f

    @property
    def fillOpacity(self):
        return self.data["fill-opacity"]

    @fillOpacity.setter
    def fillOpacity(self, f):
        self.data["fill-opacity"] = f

    @property
    def stroke(self):
        return self.data["stroke"]

    @stroke.setter
    def stroke(self, f):
        self.data["stroke"] = f

    @property
    def strokeOpacity(self):
        return self.data["stroke-opacity"]

    @strokeOpacity.setter
    def strokeOpacity(self, f):
        self.data["stroke-opacity"] = f

    @property
    def strokeWidth(self):
        return self.data["stroke-width"]

    @strokeWidth.setter
    def strokeWidth(self, f):
        self.data["stroke-width"] = f

    @property
    def data(self):
        return self._data


