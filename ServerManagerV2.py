import os, sys
import string
import numpy as np


Starters = ("startServer.sh","StartServer.sh","ServerStart.sh","launch.sh","ServerStartLinux.sh") #if you want more add more
lineArt = "-+========================+-"

print(os.getcwd()) #this be where we be

folder = os.getcwd()
folder = os.path.join(folder,'servers')

sub_folders = [name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))]

print(sub_folders)

def ScanServerFiles():


    return

def FindServerPorts():

    return
def CheckOnlineServers():

    return

def SendServerCommand():

    return

def ListArray():

    return

def TestFile():

    return

def FindStarter():

    return
def StartServers():

    return
def StopServers():

    return

def MainMenu():

    return
def StartServerMenu():

    return

def StopServerMenu():

    return

def ValidateUserInput():

    return