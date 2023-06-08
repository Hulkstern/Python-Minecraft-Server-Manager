import os
import modules.core as core

#Functions
def ScanServerFiles():

    return

def FindServerPorts(ServerName):
    #Going to scan the server.properties file till a line containing "server-port" is found, that value is what we shall return
    return

def SendServerCommand(ServerName, ServerCommand):
    os.system(f"screen -S {ServerName} -X {ServerCommand}")
    return

