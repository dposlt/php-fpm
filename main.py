#!/usr/bin/env python

import sys, os, configparser




class Environment:
    '''
    def __init__(self, path):
        self.path = path
'''

    #def setPath():
    def __init__(self):

        config = configparser.ConfigParser()
        config.read('settings.ini')
        section = config.sections()

        if 'PHP_PATH' in section:
            path = config['PHP_PATH']['path']
            _filesPath = config['PHP_PATH']['filePath']

            self.path = path
            self.files = _filesPath

    def getPyVersion(self):

        version = '3.6'
        if sys.version >= version:
            pass
        else:
            print('Your python version is old. Requirement 3.6 or hight')
            print('Your currently version is: {}'.format(sys.version))
            sys.exit()

    
    def verify(self):
        if os.path.exists(self.path):
            return self.path
        else:
            print("Path {} doesn't exist, plese verify settings".format(self.path))


    def verifyFiles(self):

        if os.path.isfile(self.files):
            return self.files
        else:
            print('No files')


    def listPHP(self):
        if self.verify(): os.chdir(self.verify())
        #if Environment.verify(None): os.chdir(Environment.verify())
        #print([d for d in os.listdir('.') if os.path.isdir(d)])
        dirname = []
        for dir in os.listdir('.'):
            if os.path.isdir(dir):  #jen adresare
                if 'php' in dir:    #jen php adresare
                    dirname.append(dir)
        return dirname


    def choisePHP(self):
        #dirname, countdir = Environment.listPHP(None)

        dirname = self.listPHP()


        for index, d in enumerate(dirname):
            print('Press {index} for {dirname} '.format(index = index, dirname = d))

        try:
            choise = int(input())
            os.chdir(dirname[choise])
        except:
            print('Must be integer')
            exit()

    def wfiles(self):
        try:
            self.choisePHP()
            if self.verifyFiles():
                with open(self.verifyFiles()) as conf:
                    conf.read()
        except:
            return 'Method is not read'
        #Environment.verifyFiles()


E = Environment()
E.getPyVersion()

E.wfiles()
