#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#*********************************************************************************************************
#*   __     __               __     ______                __   __                      _______ _______   *
#*  |  |--.|  |.---.-..----.|  |--.|   __ \.---.-..-----.|  |_|  |--..-----..----.    |       |     __|  *
#*  |  _  ||  ||  _  ||  __||    < |    __/|  _  ||     ||   _|     ||  -__||   _|    |   -   |__     |  *
#*  |_____||__||___._||____||__|__||___|   |___._||__|__||____|__|__||_____||__|      |_______|_______|  *
#* http://www.blackpantheros.eu | http://www.blackpanther.hu - kbarcza[]blackpanther.hu * Charles Barcza *
#*                                                                                                       *
#*                      Written by Miklos Horvath * hmiki[]blackpantheros.eu                             *
#*                                                                                                       *
#*************************************************************************************(c)2002-2017********

from distutils.core import setup
from distutils.command.install_data import install_data
from distutils.dep_util import newer
import os

PO_DIR = 'po'

class InstallData(install_data):
    def run(self):
        self.data_files.extend(self.compile_po_files())
        install_data.run(self)
        
    def compile_po_files(self):
        data_files = []
        if not os.path.exists('messages.pot'):
            os.system("./Messages.sh")
        if not os.path.exists(PO_DIR):
            os.makedirs(PO_DIR)
        for lang in open('languages', 'r').readlines():
            lang = lang.strip()
            if lang:
                po = os.path.join(PO_DIR, lang+'.po')                

                if not os.path.exists(po):
                    os.system('msginit --no-translator -i messages.pot -o {} -l {}.UTF-8'.format(po, lang))
                    
                mo = os.path.join('build', 'share', 'locale', lang, 'LC_MESSAGES', 'espeak-qtgui.mo')
                directory = os.path.dirname(mo)                

                if not os.path.exists(directory):
                    os.makedirs(directory)
            
                if newer(po, mo):
                    cmd = 'msgfmt -o {} {}'.format(mo, po)
                    os.system(cmd)
                
                dest = os.path.dirname(os.path.join('share', 'locale', lang, 'LC_MESSAGES', 'espeak-qtgui.mo'))
                data_files.append((dest, [mo]))
            
        return data_files

setup(name='espeak-qtgui',
      version='1.0',
      description='Qt5 Gui for Espeak',
      author='Miklos Horvath',
      author_email='hmiki@blackpantheros.eu',
      url='https://github.com/hmikihth/espeak-qtgui/',
      packages=['espeak_qtgui', 'espeak_qtgui.ui', 'espeak_qtgui.engines'],
      scripts=['espeak-qtgui'],
      data_files=[('share/applications',['espeak-qtgui.desktop'])],
      cmdclass={'install_data': InstallData}
     )
