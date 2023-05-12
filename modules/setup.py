import os
import modules.ui as ui
from decouple import config

serversDir = os.path.join(os.getcwd(), config('serversDirectory'))

def init():
    if not os.path.exists(serversDir):
        print("servers directory does not exist, creating...")
        os.mkdir(serversDir)
        print(str(serversDir)+" created, creating sampleServer directory...")
        os.mkdir(os.path.join(serversDir,'sampleServer'))
        basicStartScript('sampleServer')
        print("sampleServer directory and start script created, Visit: "+ui.link("https://www.minecraft.net/en-us/download/server")+" to download the most recent server.jar to the sampleServer directory to get started")

def make_executable(path):
    mode = os.stat(path).st_mode
    mode |= (mode & 0o444) >> 2    # copy R bits to X
    os.chmod(path, mode)

def basicStartScript(serverStartDir):
    scriptLoc = os.path.join(serversDir,serverStartDir,"startServer.sh")
    script = open(scriptLoc, 'w')
    script.write("java -Xmx1G -Xms1G -jar server.jar")
    script.close()
    make_executable(scriptLoc)