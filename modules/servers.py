import os
import modules.core as core
import modules.server as svr
from decouple import config

cwd = os.getcwd()
serversDir = os.path.join(cwd,config('serversDirectory')) # type: ignore

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
        starter = core.findStarter(serverName)
        if starter != False:
            os.chdir(os.path.join(serversDir,serverName))
            os.system("screen -d -m -S {serverName} {starter}")
    os.chdir(cwd)

    return

def stop(serverName):
    svr.SendServerCommand(serverName, "stop")
    return

def listem():
    return list([name for name in os.listdir(serversDir) if os.path.isdir(os.path.join(serversDir, name))])