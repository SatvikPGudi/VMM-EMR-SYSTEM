import subprocess
import sys

PACKAGES = ["flask", "markupsafe"]

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install(" ".join(PACKAGES))
