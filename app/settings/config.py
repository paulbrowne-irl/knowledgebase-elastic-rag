import configparser

'''
Loads the config in a way that it can be overwritten
see settings-overwrite.note
'''

config = configparser.ConfigParser()
config.read(['app/settings/settings.conf', 'app/settings/settings-overwrite.conf'])


def read (ConfigKey):

    ''''
    Find the relevant value in settings matching the config key - return a string
    '''

    settings=config['SETTINGS']
    return settings[ConfigKey]

def read_int (ConfigKey):

    ''''
    Find the relevant value in settings matching the config key - return an int
    '''

    settings=config['SETTINGS']
    return settings.getint(ConfigKey)

def read_boolean (ConfigKey):

    ''''
    Find the relevant value in settings matching the config key - return a boolean
    '''

    settings=config['SETTINGS']
    return settings.getboolean(ConfigKey)