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
            path = config['PHP_PATH']['path']
            pathfile = config['PHP_PATH']['filePath']
            return path, pathfile

    def getPyVersion(self):

        version = '3.6'
        if sys.version >= version:
            pass
        else:
            print('Your python version is old. Requirement 3.6 or hight')
            print('Your currently version is: {}'.format(sys.version))
            sys.exit()


    def verifyPath():
        path, pathfile = Environment.setPath()
        if os.path.exists(path):
            return path
        else:
            print("Path {} doesn't exist, plese verify settings".format(path))

    def verifyFiles():
        path, pathfile = Environment.setPath()

        if os.path.isfile(pathfile):
            print(True)
        else:
            print('none')


    def listPHP():
        #path, pathfile = Environment.setPath()
        if Environment.verifyPath(): os.chdir(Environment.verifyPath())
        #print([d for d in os.listdir('.') if os.path.isdir(d)])
        dirname = []
        for dir in os.listdir('.'):
            if os.path.isdir(dir):  #jen adresare
                if 'php' in dir:    #jen php adresare
                    dirname.append(dir)
        return dirname


    def choisePHP():
        #dirname, countdir = Environment.listPHP(None)
        dirname = Environment.listPHP()

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
        Environment.choisePHP()

        Environment.verifyFiles()


E = Environment()
E.getPyVersion()
E.wfiles()
#E.verifyFiles()