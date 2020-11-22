import copy 
from theme import Theme

class GeoParser:
    def __init__(self, geo):
        self.geo = geo

    @property
    def profile(self):
        return self.geo["profile"]

    @property
    def name(self):
        return self.profile["geography"]["name"]

    @property
    def level(self):
        return self.profile["geography"]["level"]
    
    @property
    def parents(self):
        return self.profile["geography"]["parents"]

    @property
    def parent(self):
        parents = self.profile["geography"]["parents"]
        if len(parents) > 0:
            return parents[-1]

        return None
        
    @property
    def profile_data(self):
        return self.profile["profile_data"]

    @property
    def profile_categories(self):
        return self.profile_data.keys()

    def category_data(self, category):
        return self.profile_data[category]

    def _subcategories(self, category):
        return self.category_data(category)["subcategories"]

    def subcategory_data(self, category, subcategory):
        return self._subcategories(category)[subcategory]

    def profile_subcategories(self, category):
        return self._subcategories(category).keys()

    def _indicators(self, category, subcategory):
        return self.subcategory_data(category, subcategory)["indicators"]

    def indicators(self, category, subcategory):
        return self._indicators(category, subcategory).keys()

    def indicator_data(self, category, subcategory, indicator):
        return self._indicators(category, subcategory)[indicator]

    def data(self, category, subcategory, indicator):
        d = copy.deepcopy(self.indicator_data(category, subcategory, indicator))
        subindicators = d["subindicators"]
        for s in subindicators.items():
            del s[1]["children"]

        values = [(subindicator, v["count"]) for subindicator, v in subindicators.items()] 

        return values

    @property
    def parent_layers(self):
        return self.geo["parent_layers"]

    @property
    def parent_layer(self):
        parent_code = self.parent["code"]
        layers = self.parent_layers

        if len(layers) >= 2:
            parent_features = layers[-2]["features"]
            for feature in parent_features:
                if feature["properties"]["code"] == parent_code:
                    return feature


    @property
    def themes(self):
        return [Theme(js) for js in self.geo["themes"]]

    @property
    def boundary(self):
        return self.geo["boundary"]


    @property
    def name(self):
        return self.profile["geography"]["name"]
        
    @property
    def level(self):
        return self.profile["geography"]["level"]


