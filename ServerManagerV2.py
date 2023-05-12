import os, sys
import string
import numpy as np
import modules.server as svr
import modules.servers as svrs
import modules.ui as ui
from decouple import config

lineArt = "-+========================+-"
cwd = os.getcwd()
serversDir = os.path.join(cwd,'servers')

#print(os.getcwd()) #this be where we be

#Initial Setup
if not os.path.exists(serversDir):
    print("servers directory does not exist, creating...")
    os.mkdir(serversDir)
    print("server directory created, visit: "+ui.link("https://www.minecraft.net/en-us/download/server")+" to download the most recent server.jar to the sampleServer directory to get started")

print(os.path.join(cwd,'servers'))
folder = os.path.join(cwd,'servers')

sub_folders = [name for name in os.listdir(serversDir) if os.path.isdir(os.path.join(serversDir, name))]

print(sub_folders)