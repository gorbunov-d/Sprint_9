import shutil
import subprocess
import sys
from pathlib import Path
from urllib.request import urlopen

from selenium.webdriver.support.ui import WebDriverWait


def selenoid_ready(_):
    try:
        with urlopen("http://selenoid:4444/status", timeout=3) as response:
            return response.status == 200
    except OSError:
        return False


WebDriverWait(None, 60, poll_frequency=1).until(selenoid_ready)
results = Path(__file__).resolve().parents[1] / "allure-results"
results.mkdir(exist_ok=True)
for artifact in results.iterdir():
    if artifact.is_dir() and not artifact.is_symlink():
        shutil.rmtree(artifact)
    else:
        artifact.unlink()
sys.exit(subprocess.call(["pytest", *sys.argv[1:]]))
