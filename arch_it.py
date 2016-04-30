import os
import subprocess
from datetime import datetime

from lat_plaza import get_statuses
from settings import BASE_DIR

get_statuses()

os.chdir(BASE_DIR)
subprocess.call(["git", "add", "."])
subprocess.call("git commit -am \"{}\"".format(datetime.now().isoformat()).split())
subprocess.call(["git", "push", "plaza", "data"])
