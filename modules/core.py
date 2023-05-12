#Imports
import os
from decouple import config
from decouple import Csv

#Needed Variables
cwd = os.getcwd()
serversDir = os.path.join(cwd,config('serversDirectory')) #type: ignore
starters = (config('starters',cast=Csv(post_process=list))) #type: ignore
lineArt = config('lineArt')

#Functions