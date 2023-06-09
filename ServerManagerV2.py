import os
#import numpy as np
import modules.server as svr
import modules.servers as svrs
import modules.ui as ui
import modules.setup as setup
import modules.core as core

loopMenuState = True

#Initial Setup
setup.init()

print(os.path.join(core.cwd,core.serversDir))
folder = os.path.join(core.cwd,core.serversDir)

sub_folders = [name for name in os.listdir(core.serversDir) if os.path.isdir(os.path.join(core.serversDir, name))]

while loopMenuState:
    userInput = ui.MainMenu()
    print("")
    match ui.ValidateUserInput(userInput, "mainMenu"):
        case 1:
            while True:
                svrStartInput = ui.ValidateUserInput(ui.StartServerMenu(),"serverStart")
                if svrStartInput==False:
                    print("Please Try Again")
                else:
                    for index, eachVal in enumerate(svrStartInput): #type: ignore
                        svrStartInput[index]=svrs.listem()[eachVal-1] #type: ignore
                    svrs.start(svrStartInput)
                    break
        case 2:
            ui.StopServerMenu()
        case 3:
            print("Functionality will be added soon")
        case 4:
            loopMenuState=False
        case False:
            ui.error(userInput,0)

#print(svrs.findStarter(svrs.listem()[0]))