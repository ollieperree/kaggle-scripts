from os import system
from pathlib import Path
import json


def setup(competition_name, path, ram_gb=32):
    path = Path(path)

    path_data = path/"data"
    (path_data).mkdir(parents=True)
    system(f"kaggle competitions download {competition_name} -p {path_data.absolute()}")

    (path/"config").mkdir(parents=True)
    settings = dict(competition_name=competition_name, ram_gb=ram_gb)
    (path/"config/config.txt").touch()
    with open(path/"config/config.txt", "w") as f:
        f.write(json.dumps(settings))

    path_scripts = path/"scripts"
    (path_scripts).mkdir(parents=True)
    # Download latest version of kaggle scripts into path/scripts
    system(f"git clone https://github.com/ollieperree/kaggle-scripts.git {path_scripts}")

    (path/"models").mkdir(parents=True)

    (path/"features").mkdir(parents=True)
