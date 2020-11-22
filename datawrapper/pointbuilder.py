from pointmarker import PointMarker

class PointBuilder:
    def __init__(self, dw):
        self.dw = dw

    def generate_markers(self, points_geojson):
        markers = []
        features = points_geojson["features"]

        for point in features:
            name = point["properties"]["name"]
            coordinates  = point["geometry"]["coordinates"]
            longitude, latitude = coordinates
            marker = PointMarker(name, latitude, longitude)
            marker.color = "#ff0000"
            markers.append(marker.data)

        return markers


