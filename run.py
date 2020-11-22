import json
import sys

from slugify import slugify

from polygon import Polygon
from wazimap import GeoParser, load_geo, load_points

from datawrapper import PointBuilder
from datawrapper import Datawrapper
from datawrapper import Metadata
from datawrapper import BoundaryMarker

data_wrapper_auth = open("credentials").read().strip()

dw = Datawrapper(access_token=data_wrapper_auth)

code = sys.argv[1]
profile = sys.argv[2]
subcategory = sys.argv[3]
chart_id = sys.argv[4]

chart_json = dw.chart_properties(chart_id)

parser = load_geo(code, profile)
chart_title = parser.name

themes = parser.themes

polygon = Polygon(parser.boundary)
boundary_marker = BoundaryMarker(parser.name)
boundary_marker.coordinates = polygon.coordinates
properties = boundary_marker.properties
properties.stroke = "black"
properties.strokeWidth = 3


chart_json["markers"] = [boundary_marker.data]

for theme in themes:
    for subtheme in theme.subthemes:
        if str(subtheme["id"]) == subcategory: 
            points = load_points(code, profile=profile, category=subcategory)
            subtheme_label = subtheme["label"]
            pointBuilder = PointBuilder(dw)
            markers = pointBuilder.generate_markers(points)
            chart_json["markers"].extend(markers)
            chart_title = f"{subtheme_label} in {parser.name}"
            
zoom_lookup = {
    "province": 6,
    "district": 7,
    "municipality": 8,
    "mainplace": 9,
}


zoom = zoom_lookup.get(parser.level, 7)
parent_geography = parser.parents[-1]
metadata = Metadata(chart_json["metadata"])
metadata.set_view(zoom, polygon.centroid(), 0)
metadata.set_intro(f"{parser.name} is a {parser.level} in {parent_geography['name']} {parent_geography['level']}")
metadata.notes = f"{parser.name} is a {parser.level} in {parent_geography['name']} {parent_geography['level']}"
metadata.style = Metadata.STYLE_LIGHT


if len(parser.parent_layers) >= 2:
    parent_feature = parser.parent_layer
    if parent_feature is not None:
        dw.set_minimap(chart_id, parent_feature["geometry"])
        metadata.minimap["label"] = parent_geography["name"]
        metadata.minimap["type"] = "custom"
    
dw.set_data(chart_id, {"markers": chart_json["markers"]})
dw.update_chart(chart_id, {"title": chart_title, "metadata": metadata.metadata})
dw.export_chart(chart_id, filepath=f"{slugify(parser.name)}.png" )

