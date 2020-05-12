#!/usr/bin/env python3
from BitcoinKeyMailer import BitcoinKeyMailer
from BitcoinKeyGenerator import BitcoinKeyGenerator
from BitcoinKeyChecker import BitcoinKeyChecker
from BitcoinKeySaver import BitcoinKeySaver
import json
import os


class BitcoinFinder():
    
    def __init__(self):
        self.env = None
        self.addresses = None
        self.BitcoinKeyChecker = None
        self.numTries = 1000
        self.i = 0
    
    def setEnv(self, env):
        self.env = env
        
    def setNumTimes(self, num):
        self.numTries = num    
    
    def setAddressList(self, addresses):
        self.addresses = addresses 
        self.BitcoinKeyChecker = BitcoinKeyChecker(addresses)   
    
    def start(self):
        self.variableCheck()
        while self.i < self.numTries:
            # GENERATE PUBLIC KEYS
            generator = BitcoinKeyGenerator();
            pubKey1 = generator.bitcoinAddress
            pubKey2 = generator.bitcoinAddress2
            pubKey3 = generator.compressedBitcoinAddress
            # CHECK PUBLIC KEYS
            check1 = self.BitcoinKeyChecker.checkList(pubKey1)
            check2 = self.BitcoinKeyChecker.checkList(pubKey2)
            check3 = self.BitcoinKeyChecker.checkList(pubKey3)
            # if public keys match one of the keys on the list, save/send all public/private key formats
            match1 = self.saveIfMatch(check1, generator)
            match2 = self.saveIfMatch(check2, generator) 
            match3 = self.saveIfMatch(check3, generator)  
            #PRINT AND INCRIMENT
            if self.i % 10 == False:
                print(self.i)
                pass
            self.i = self.i + 1
            del generator
        if match1 == True or match2 == True or match3 == True :
            print("MATCH FOUND!!!!!!") 
        else:
            print("NO MATCHES FOUND")      
          
    
    def variableCheck(self):
        if self.addresses == None:
            print("addresses not set --- addresses check failed in variableCheck function")
            print("**********************************************************")
            raise  
        if self.BitcoinKeyChecker == None:
            print("BitcoinKeyChecker not set --- BitcoinKeyChecker check failed in variableCheck function")
            print("**********************************************************")
            raise 
        if self.numTries < 1:
            print("Number of times is 0 or less - make sure to set the number of times you want this to run")
            print("**********************************************************")
            raise         
            
    def saveIfMatch(self, match, generator):
        if match:
            json_data = json.dumps(generator.__dict__)
            print("MATCH FOUND!!!!!!!!!!!!!!!!!!!!!!! " + json_data)
            self.sendEmail(json_data)
            self.saveData(json_data)
            return True
        else:
            return False    
    
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
           
          