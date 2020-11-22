from geojson_utils import centroid

class Polygon:
    def __init__(self, geojson):
        self.geojson = geojson

    @property
    def geometry(self):
        return self.geojson["geometry"]

    @property
    def coordinates(self):
        return self.geojson["geometry"]["coordinates"][0]

    def centroid(self):
        coordinates = self.geometry["coordinates"]
        if self.geometry["type"] == "MultiPolygon":
            coordinates = coordinates[0]
        c = centroid({"coordinates": coordinates})["coordinates"]

        return c

