import configparser
import logging

'''
Loads the config in a way that it can be overwritten
see settings-overwrite.note
'''

config = configparser.ConfigParser()
config.read(['settings/config.conf', 'settings/config-overwrite.conf'])


def read (ConfigKey:str)->str:
    ''''
    Find the relevant value in settings matching the config key - return a string
    '''
    settings=config['SETTINGS']
    returnObj= settings.get(ConfigKey)


    return returnObj

def read_int (ConfigKey:str)->int:

    ''''
    Find the relevant value in settings matching the config key - return an int
    '''

    settings=config['SETTINGS']
    return settings.getint(ConfigKey)

def read_boolean (ConfigKey:str)->bool:

    ''''
    Find the relevant value in settings matching the config key - return a boolean
    '''

    settings=config['SETTINGS']
    return settings.getboolean(ConfigKey)



def read_dict (ConfigKey:str)->dict:

    ''''
    Find the relevant value in settings matching the config key - return a dictionary of values
    '''

    settings=config[ConfigKey]
    return settings