#Imports
import os
import bison
from decouple import config
from decouple import Csv

#Needed Variables
cwd = os.getcwd()
serversDir = os.path.join(cwd,config('serversDirectory')) #type: ignore
starters = (config('starters',cast=Csv(post_process=list))) #type: ignore
#mainMenuOpt = (config('mainMenuOpt',cast=Csv(post_process=list))) #type: ignore
lineArt = config('lineArt')

""" script_config_scheme = bison.Scheme(
    bison.DictOption('settings', scheme=bison.Scheme(
        bison.Option('servers_directory',required=False,default=str("servers"),field_type=str), #type: ignore
        bison.ListOption('starters',required=False,default=str("['startServer.sh','StartServer.sh','ServerStart.sh','launch.sh','ServerStartLinux.sh']"),member_type=str) #type: ignore
    )),
    bison.DictOption('program_setup', scheme=bison.Scheme(
        bison.ListOption('main_menu_opt',required=False,default=str("['Start Servers','Stop Servers','Send Command','Exit Program']"),member_type=str) #type: ignore
    ))
)
script_config = bison.Bison(scheme=script_config_scheme)
script_config.config_name = 'script_config'
script_config.add_config_paths(str(cwd)+'/config/')
script_config.parse()

script_config.env_prefix = 'MCSM' # type: ignore
config.auto_env = True # type: ignore """

#Functions
def printVar(var):
    variable_name = [k for k, v in locals().items() if v == var][0] 
    print(str(variable_name)+": "+str(var))
    return

#printVar(mainMenuOpt)

#testVar = script_config.get('settings.servers_directory')