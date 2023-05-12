import modules.core
import os
from decouple import config

#Functions
def ScanServerFiles():

    return

def FindServerPorts():

    return

def SendServerCommand(ServerName, ServerCommand):
    os.sys("screen -S {ServerName} -X {ServerCommand}")
    return

