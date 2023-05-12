import os
from decouple import config
from decouple import Csv
from pathlib import Path
cwd = os.getcwd()

starters = (config('starters',cast=Csv()))
def findStarter(serverDir):
    for value in starters:
        if (Path(os.path.join(cwd,'servers',serverDir,value))).is_file():
            return value
    return False