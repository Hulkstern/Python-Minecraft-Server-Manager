import os
import numpy as np
import modules.server as svr
import modules.servers as svrs
import modules.ui as ui
import modules.setup as setup
import modules.core as core
from decouple import config

cwd = os.getcwd()
serversDir = os.path.join(cwd,'servers')

#Initial Setup
setup.init()

print(os.path.join(cwd,'servers'))
folder = os.path.join(cwd,'servers')

sub_folders = [name for name in os.listdir(serversDir) if os.path.isdir(os.path.join(serversDir, name))]

print(sub_folders)

print(core.findStarter(sub_folders[1]))