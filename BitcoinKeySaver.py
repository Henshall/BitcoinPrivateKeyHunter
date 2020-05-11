#!/usr/bin/env python3
import env

class BitcoinKeySaver():
    """docstring for BitcoinKeyMailer."""

    def __init__(self):        
        self.env = None 
        self.dataString = None 
    
    def setEnv(self, env):        
        self.env = env
        
    def setDataString(self, string):        
        self.dataString = string    
        
    def save(self):
        fl = open(env.KEYS_FOUND_TEXT_FILE_NAME, "a")
        fl.write("FOUND SOMETHING INTERESTING \n")
        fl.write("KEY INFO = " + self.dataString + "\n")
        fl.write("NOTE: PUBLIC KEY MAY NEED TO BE ALL UPPER CASE")
        fl.close()
        