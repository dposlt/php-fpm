#!/usr/bin/env python

import sys, os, configparser


class Environment:
    '''
    def __init__(self, path):
        self.path = path
'''

    # def setPath():
    def __init__(self):

        config = configparser.ConfigParser()
        config.read('settings.ini')
        section = config.sections()

        if 'PHP_PATH' in section:
            _php_path = config['PHP_PATH']['php_path']
            _filesPath = config['PHP_PATH']['wwwConfPath']
            _nls = config['PHP_PATH']['nls_lang']
            _php_fpm = config['PHP_PATH']['php_fpm_conf']
            _php_error = config['PHP_PATH']['php_error']

            self.php_path = _php_path
            self.files = _filesPath
            self.nls = _nls
            self.php_fpm = _php_fpm
            self.php_error = _php_error

    def getPyVersion(self):

        version = '3.6'
        if sys.version >= version:
            pass
        else:
            print('Your python version is old. Requirement 3.6 or hight')
            print('Your currently version is: {}'.format(sys.version))
            sys.exit()

    def verify(self):
        if os.path.exists(self.php_path):
            return self.php_path
        else:
            print("Path {} doesn't exist, plese verify settings".format(self.php_path))
            exit()

    def verifyFiles(self, files):
        self.files = files
        if os.path.isfile(files):
            return True
        else:
            print('No files')

    def listPHP(self):
        if self.verify(): os.chdir(self.verify())
        # if Environment.verify(None): os.chdir(Environment.verify())
        # print([d for d in os.listdir('.') if os.path.isdir(d)])
        dirname = []
        for dir in os.listdir('.'):
            if os.path.isdir(dir):  # jen adresare
                if 'php' in dir:  # jen php adresare
                    dirname.append(dir)
        return dirname

    def choisePHP(self):
        # dirname, countdir = Environment.listPHP(None)

        dirname = self.listPHP()

        countIndex = 0
        for index, d in enumerate(dirname):
            print('Press {index} for {dirname} '.format(index=index + 1, dirname=d))
            countIndex +=1

        try:
            choise = int(input())

            for i in range(countIndex):
                if i == choise:
                    os.chdir((dirname[choise]))
        except:
            print('Must be integer')
            exit()

    def writeNLSfiles(self):
        try:
            self.choisePHP()
            if self.verifyFiles(self.files):
                with open(self.files, 'r+') as conf:
                    line_found = any(self.nls in line for line in conf)
                    if not line_found:
                        conf.seek(0, os.SEEK_END)
                        conf.write(f'\n{self.nls}')

            if self.verifyFiles(self.php_fpm):
                with open(self.php_fpm, 'r+') as conf:
                    line_found = any(self.php_error in line for line in conf)
                    if not line_found:
                        conf.seek(0, os.SEEK_END)
                        conf.write(f'\n{self.php_error}')
        except:
            return 'Method is not read'
        # Environment.verifyFiles()



E = Environment()
E.getPyVersion()

E.writeNLSfiles()
#E.writePHP_fpm_Files()
