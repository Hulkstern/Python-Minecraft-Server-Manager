import modules.core
from decouple import config

lineArt = config('lineArt')

#Functions
def MainMenu():

    return

def StartServerMenu():

    return

def StopServerMenu():

    return

def ValidateUserInput():

    return

def link(uri, label=None):
    if label is None: 
        label = uri
    parameters = ''

    # OSC 8 ; params ; URI ST <name> OSC 8 ;; ST 
    escape_mask = '\033]8;{};{}\033\\{}\033]8;;\033\\'

    return escape_mask.format(parameters, uri, label)