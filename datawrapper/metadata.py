class Metadata:
    STYLE_EARTH = "dw-earth"
    STYLE_LIGHT = "dw-light"
    STYLE_GRAY = "dw-gray"
    STYLE_MARITIME = "dw-maritime"

    def __init__(self, metadata):
        self._metadata = metadata

    @property
    def metadata(self):
        return self._metadata

    def set_view(self, zoom, center, pitch):
        self.metadata["visualize"]["view"]["center"] = center
        self.metadata["visualize"]["view"]["pitch"] = pitch
        self.metadata["visualize"]["view"]["zoom"] = zoom


    def set_intro(self, intro):
        self.metadata["describe"]["intro"] = intro

    @property
    def minimap(self):
        return self.metadata["visualize"]["miniMap"]


    @property
    def style(self):
        return self.metadata["visualize"]["style"]


    @style.setter
    def style(self, s):
        self.metadata["visualize"]["style"] = s


    @property
    def notes(self):
        return self.metadata["annotate"]["notes"]

    @notes.setter
    def notes(self, text):
        self.metadata["annotate"]["notes"] = text
