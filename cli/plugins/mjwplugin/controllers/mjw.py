from .template import TemplateHandler


class MJWHandler:
    def __init__(self, app):
        self.template = TemplateHandler(app)
