#!/usr/bin/env python

import sys, os, configparser

class Environment:
    '''
    def __init__(self, path):
        self.path = path
'''

    def setPath():
        config = configparser.ConfigParser()
        config.read('settings.ini')
        section = config.sections()

        if 'PHP_PATH' in section:
            return  config['PHP_PATH']['path']

    def getPyVersion(self):

        version = '3.6'
        if sys.version >= version:
            pass
        else:
            print('Your python version is old. Requirement 3.6 or hight')
            print('Your currently version is: {}'.format(sys.version))
            sys.exit()


    def verifyPath():
        if os.path.exists(Environment.setPath()):
            return Environment.setPath()
        else:
            print("Path {} doesn't exist, plese verify settings".format(Environment.setPath()))



    def listPHP(self):
        if Environment.verifyPath(): os.chdir(Environment.setPath())
        #print([d for d in os.listdir('.') if os.path.isdir(d)])
        dirname = []
        for dir in os.listdir('.'):
            if os.path.isdir(dir):  #jen adresare
                if 'php' in dir:    #jen php adresare
                    dirname.append(dir)
        return dirname


    def choisePHP():
        #dirname, countdir = Environment.listPHP(None)
        dirname = Environment.listPHP(None)

        for index, d in enumerate(dirname):
            print('Press {index} for {dirname} '.format(index = index, dirname = d))

        try:
            choise = int(input())
            os.chdir(dirname[choise])
            return os.getcwd()
        except:
            print('Must be integer')
            exit()

    def wfiles(self):
        pass


E = Environment()
E.getPyVersion()
E.choisePHP()