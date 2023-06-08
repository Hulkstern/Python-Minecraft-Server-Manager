import modules.core as core
import modules.servers as svrs

#Functions
def MainMenu():
    print("\nWhadya want?")
    print("1. Start Servers")
    print("2. Stop Servers")
    print("3. Send Command to Server")
    print("4. Exit Program")
    return input("Choose a number:\n")

def StartServerMenu():
    output=""
    for index, curServer in enumerate(svrs.listem()):
        output=output+str("%3d"%(index+1))+f" - {curServer[0:-4]}\n"
    print(f"Available Servers:\n{output}")
    return

def StopServerMenu():

    return

def ValidateUserInput(userInput, inType):
    match inType:
        case "mainMenu":
            print("Validating input")
            try:
                return int(userInput)
            except:
                return False
    #return userInput

def error(issueText, errorType):
    match errorType:
        case 0: #Invalid Input
            print(f"The input \"{issueText}\" is not valid, please enter the number of your selection and press enter.")
        case 1: #out of bounds input
            print()

def link(uri, label=None):
    if label is None: 
        label = uri
    parameters = ''

    # OSC 8 ; params ; URI ST <name> OSC 8 ;; ST 
    escape_mask = '\033]8;{};{}\033\\{}\033]8;;\033\\'

    return escape_mask.format(parameters, uri, label)