import glob
from os.path import dirname, basename, isfile, join

# Ye code apne aap sari .py files ko load kar lega
modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py') and not f.endswith('__main__.py')]
