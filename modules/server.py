import os
import modules.core as core

#Functions
def ScanServerFiles():

    return

def FindServerPorts():

    return

def SendServerCommand(ServerName, ServerCommand):
    os.system("screen -S {ServerName} -X {ServerCommand}")
    return

