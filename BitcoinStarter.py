#!/usr/bin/env python3
from BitcoinKeyMailer import BitcoinKeyMailer
from BitcoinKeyGenerator import BitcoinKeyGenerator
from BitcoinKeyChecker import BitcoinKeyChecker
from BitcoinKeySaver import BitcoinKeySaver
import json

class BitcoinStarter():
    
    def __init__(self):
        self.env = None
        self.addresses = None
        self.BitcoinKeyChecker = None
        self.numTries = 100
        self.i = 0
    
    def setEnv(self, env):
        self.env = env
    
    def setAddressList(self, addresses):
        self.addresses = addresses 
        self.BitcoinKeyChecker = BitcoinKeyChecker(addresses)   
    
    def start(self):
        self.variableCheck()
        while self.i < self.numTries:
            # GENERATE PUBLIC KEYS
            generator = BitcoinKeyGenerator();
            pubKey1 = generator.bitcoinAddress
            pubKey2 = generator.compressedBitcoinAddress
            # CHECK PUBLIC KEYS
            check1 = self.BitcoinKeyChecker.checkList(pubKey1)
            check2 = self.BitcoinKeyChecker.checkList(pubKey2)
            # if public keys match one of the keys on the list, save/send all public/private key formats
            self.saveIfMatch(check1, generator)
            self.saveIfMatch(check2, generator)  
            self.i = self.i + 1
            del generator
    
    def variableCheck(self):
        if self.env == None:
            print("env not set --- env check failed in variableCheck function")
            print("**********************************************************")
            raise
        if self.addresses == None:
            print("addresses not set --- addresses check failed in variableCheck function")
            print("**********************************************************")
            raise  
        if self.BitcoinKeyChecker == None:
            print("BitcoinKeyChecker not set --- BitcoinKeyChecker check failed in variableCheck function")
            print("**********************************************************")
            raise     
            
    def saveIfMatch(self, match, generator):
        if match:
            json_data = json.dumps(generator.__dict__)
            print("KEY FOUND!!!!!!!!!!!!!!!!!!!!!!! " + json_data)
            self.sendEmail(json_data)
            self.saveData(json_data)
        else:
            print("key not found, i = " + str(self.i))
            pass    
    
    def sendEmail(self, data):
        try:
            mailer = BitcoinKeyMailer()
            mailer.setEnv(self.env)
            mailer.setText("BitcoinKeyChecker Found a Matching Key Pair ---- " + data)
            mailer.send()
        except Exception as e:
            pass
            
    def saveData(self, data):
        try:
            saver = BitcoinKeySaver()
            saver.setEnv(self.env)
            saver.setDataString(data)
            saver.save() 
        except Exception as e:
            pass
           
          