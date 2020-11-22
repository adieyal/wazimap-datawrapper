import requests

from .geoparser import GeoParser

geo_url = "https://production.wazimap-ng.openup.org.za/api/v1/all_details/profile/{}/geography/{}/?format=json"
points_url = "https://production.wazimap-ng.openup.org.za/api/v1/profile/{}/points/category/{}/geography/{}/points/?format=json"

def load_geo(code, profile):
    url = geo_url.format(profile, code)
    resp = requests.get(url)
    js = resp.json()

    return GeoParser(js)

def load_points(code, category, profile):
    url = points_url.format(profile, category, code)
    resp = requests.get(url)
    js = resp.json()

    return js
