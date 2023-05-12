import modules.core as core
import modules.servers as svrs

#Functions
def MainMenu():

    return

def StartServerMenu():

    return

def StopServerMenu():

    return

def ValidateUserInput(userInput, inType):
    match inType:
        case "mainMenu":
            print("Validating input")
    return

def error(issueText, errorType):
    match errorType:
        case 0: #Invalid Input
            print("The input {issueText} is not valid, please enter the number of your selection and press enter.")
        case 1: #out of bounds input
            print()

def link(uri, label=None):
    if label is None: 
        label = uri
    parameters = ''

    # OSC 8 ; params ; URI ST <name> OSC 8 ;; ST 
    escape_mask = '\033]8;{};{}\033\\{}\033]8;;\033\\'

    return escape_mask.format(parameters, uri, label)