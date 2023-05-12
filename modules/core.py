#Imports
import os
from decouple import config
from decouple import Csv
from pathlib import Path

#Needed Variables
serversDir = os.path.join(os.getcwd(),config('serversDirectory'))
starters = (config('starters',cast=Csv()))

#Functions
def findStarter(serverDir):
    for value in starters:
        if (Path(os.path.join(serversDir,serverDir,value))).is_file():
            return value
    return False