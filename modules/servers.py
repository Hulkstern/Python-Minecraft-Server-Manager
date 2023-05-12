import os
import modules.core as core
from decouple import config

serversDir = os.path.join(os.getcwd(),config('serversDirectory'))

def checkOnline():

    return
def start():

    return
def stop():

    return

def listem():
    return list([name for name in os.listdir(serversDir) if os.path.isdir(os.path.join(serversDir, name))])