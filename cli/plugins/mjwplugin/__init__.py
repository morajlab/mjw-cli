from .controllers.mjw import MJWHandler


def extend_app(app):
    app.extend("mjw", MJWHandler(app))


def load(app):
    app.hook.register("post_setup", extend_app)
