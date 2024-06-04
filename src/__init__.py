from .utils import get_home_dir

with open("VERSION", "r") as f:
    VERSION = f.read().strip()

HOME = get_home_dir()
