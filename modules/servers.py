import os
import modules.core as core
import modules.server as svr
from pathlib import Path

#Functions
def checkOnline():
    online = []
    screenListOutput = os.popen("screen -list").read()
    for screenText in screenListOutput:
        for serInd, serVal in enumerate(listem()):
            if serVal in screenText:
                online.append([serInd,serVal])
        
    #for value in screenListOutput:
    #    if(value in listem()):
    #        online += serversDir[value]
    return online
    
def start(serverNames):
    for serverName in serverNames:
        starter = findStarter(serverName)
        if starter != False:
            os.chdir(os.path.join(core.serversDir,serverName))
            os.system("screen -d -m -S {serverName} {starter}")
    os.chdir(core.cwd)

    return

def stop(serverName):
    svr.SendServerCommand(serverName, "stop")
    return

def findStarter(serverDir):
    for starter in core.starters: #type: ignore
        if (Path(os.path.join(core.serversDir,serverDir,str(starter)))).is_file(): #type: ignore
            return starter
    return False

def listem():
    return list([name for name in os.listdir(core.serversDir) if os.path.isdir(os.path.join(core.serversDir, name))])