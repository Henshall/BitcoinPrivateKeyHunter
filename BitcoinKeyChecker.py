#!/usr/bin/env python3
import hashlib

class BitcoinKeyChecker():
    
    def __init__(self, list):
        # GENERATE PRIVATE KEYS 
        self.list = list
        
    def checkList(self, key):   
        for value in self.list:
            if key == value:
                return True
            else:
                pass
        return False
        
