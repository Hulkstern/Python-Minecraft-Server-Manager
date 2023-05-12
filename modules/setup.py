import os
import modules.ui as ui
import modules.core as core

#Functions
def init():
    if not os.path.exists(core.serversDir):
        print("servers directory does not exist, creating...")
        os.mkdir(core.serversDir)
        print(str(core.serversDir)+" created, creating sampleServer directory...")
        os.mkdir(os.path.join(core.serversDir,'sampleServer'))
        basicStartScript('sampleServer')
        print("sampleServer directory and start script created, Visit: "+ui.link("https://www.minecraft.net/en-us/download/server")+" to download the most recent server.jar to the sampleServer directory to get started")

def make_executable(path):
    mode = os.stat(path).st_mode
    mode |= (mode & 0o444) >> 2    # copy R bits to X
    os.chmod(path, mode)

def basicStartScript(serverStartDir):
    scriptLoc = os.path.join(core.serversDir,serverStartDir,"startServer.sh")
    script = open(scriptLoc, 'w')
    script.write("#!/bin/bash java -Xmx1G -Xms1G -jar server.jar")
    script.close()
    make_executable(scriptLoc)