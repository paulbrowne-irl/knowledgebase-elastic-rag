import configparser

'''
Loads the config in a way that it can be overwritten
see settings-overwrite.note
'''

config = configparser.ConfigParser()
config.read(['app/settings/settings.conf', 'app/settings/settings-overwrite.conf'])




#print(config['some-setting'])
print (config.sections())