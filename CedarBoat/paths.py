import sys, os, shutil

def resource_path(name):
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, name)

def data_path(name="boat_info"):
    if not getattr(sys, "frozen", False):      # running from PyCharm
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), name)

    folder = os.path.join(os.environ.get("APPDATA", os.path.expanduser("~")), "CedarBoat")
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, name)
    if not os.path.exists(path):               # first run of the exe: seed from bundled copy
        shutil.copy(resource_path(name), path)
    return path