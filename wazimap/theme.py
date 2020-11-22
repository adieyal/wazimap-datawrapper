class Theme:
    def __init__(self, theme):
        self._theme = theme

    @property
    def data(self):
        return self._theme


    @property
    def name(self):
        return self.data["name"]

    @property
    def id(self):
        return self.data["id"]

    @property
    def subthemes(self):
        return self.data["subthemes"]
