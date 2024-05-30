
__version__ = '0.8.0.dev0'


def setup(app, *args, **kwargs):
    from .numpydoc import setup
    return setup(app, *args, **kwargs)
