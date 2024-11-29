import configparser
import logging

'''
Loads the config in a way that it can be overwritten
see settings-overwrite.note
'''

def _get_conf_file():
    '''
    Get handle to config file, allowing for running fron project root, or within app folder
    '''
    config = configparser.ConfigParser()
    try:
        config.read(['settings/config.conf', 'settings/config-overwrite.conf'])
        settings=config['SETTINGS']
    except: 
        config.read(['app/settings/config.conf', 'app/settings/config-overwrite.conf'])
        settings=config['SETTINGS']

    return settings


def read (ConfigKey:str)->str:
    ''''
    Find the relevant value in settings matching the config key - return a string
    '''
    settings=_get_conf_file()
    returnObj= settings.get(ConfigKey)
    return returnObj

def read_int (ConfigKey:str)->int:

    ''''
    Find the relevant value in settings matching the config key - return an int
    '''

    settings=_get_conf_file()
    return settings.getint(ConfigKey)

def read_boolean (ConfigKey:str)->bool:

    ''''
    Find the relevant value in settings matching the config key - return a boolean
    '''

    settings=_get_conf_file()
    return settings.getboolean(ConfigKey)



def read_dict (config_key:str)->dict:

    ''''
    Find the relevant value in settings matching the config key - return a dictionary of values
    '''

    config = configparser.ConfigParser()
    try:
        config.read(['settings/config.conf', 'settings/config-overwrite.conf'])
        settings=config[config_key]
    except: 
        config.read(['app/settings/config.conf', 'app/settings/config-overwrite.conf'])
        settings=config[config_key]

    return dict(settings)