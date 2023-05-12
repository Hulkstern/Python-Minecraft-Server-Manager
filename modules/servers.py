import os
import modules.core as core
import modules.server as svr
from decouple import config

serversDir = os.path.join(os.getcwd(),config('serversDirectory'))

#Functions
def checkOnline():
    serverList = ""
    screenListOutput = os.popen("screen -list").read()
    for value in screenListOutput:
        if(value in listem()):
            serverList += serversDir[value]
    return serverList
    
def start(serverName):
    for value in serverName:
        starter = core.findStarter(value)
        if starter != False:
            os.sys("screen -d -m -S {value} {starter}")


    return

def stop(serverName):
    svr.SendServerCommand(serverName, "stop")
    return

def listem():
    return list([name for name in os.listdir(serversDir) if os.path.isdir(os.path.join(serversDir, name))])