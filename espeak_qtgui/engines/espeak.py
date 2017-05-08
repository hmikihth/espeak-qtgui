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

import subprocess

class Engine():
    languages = [
                 ["af", _("Afrikaans")],
                 ["bs", _("Bosnian")],
                 ["ca", _("Catalan")],
                 ["cs", _("Czech")],
                 ["da", _("Danish")],
                 ["de", _("German")],
                 ["el", _("Greek")],
                 ["en", _("English")],
                 ["eo", _("Esperanto")],
                 ["es", _("Spanish")],
                 ["es-la", _("Spanish - Latin-America")],
                 ["fi", _("Finnish")],
                 ["fr", _("French")],
                 ["hr", _("Croatian")],
                 ["hu", _("Hungarian")],
                 ["it", _("Italian")],
                 ["kn", _("Kannada")],
                 ["ku", _("Kurdish")],
                 ["lv", _("Latvian")],
                 ["nl", _("Dutch")],
                 ["pl", _("Polish")],
                 ["pt", _("Portuguese (Brazil)")],
                 ["pt-pt", _("Portuguese (European)")],
                 ["ro", _("Romanian")],
                 ["sk", _("Slovak")],
                 ["sr", _("Serbian")],
                 ["sv", _("Swedish")],
                 ["sw", _("Swahili")],
                 ["ta", _("Tamil")],
                 ["tr", _("Turkish")],
                 ]
    
    variants_male = ["m1", "m2", "m3", "m4", "m5", "m6", "m7", "croak", "wisper"]
    variants_female = ["f1", "f2", "f3", "f4", "f5", "whisperf"]
    
    sliders = {"pitch":99, "volume":200, "speed":500, "delay":200}
    
    def __init__(self):
        self.process = None
    
    def get_languages(self):
        return self.languages

    def get_variants(self, gender="male"):
        if gender == "male":
            return self.variants_male
        else:
            return self.variants_female
        
    def get_sliders(self):
        return self.sliders
 
    def play(self, text, language, pitch, volume, speed, delay, record=None):
        arguments = ["espeak", "-v", language, "-p", str(pitch), "-a", str(volume), "-s", str(speed), "-g", str(delay), "--stdout"]
        if record != None:
            arguments += ["-w", record]
        self.process = subprocess.Popen(arguments, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        self.pulse = subprocess.Popen(['paplay'], stdin=self.process.stdout)
        self.pulse.communicate()
        
        self.process.stdin.write(text.encode("utf-8"))
        self.process.stdin.flush()
        self.process.stdin.close()   
        self.process.stdout.flush()
        self.process.stdout.close()

    
    def stop(self):
        self.process.kill()
