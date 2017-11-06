import configparser

def readConfig(path = 'config.ini'):
    cfg = configparser.ConfigParser()
    print(cfg.sections())
    cfg.read('config.ini')
    print(cfg.sections())
