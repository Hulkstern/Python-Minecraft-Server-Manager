import os
from decouple import config
from decouple import Csv

starters = (config('starters',cast=Csv()))
def findStarter():

    return