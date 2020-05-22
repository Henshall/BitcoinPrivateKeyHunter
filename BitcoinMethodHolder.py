#!/usr/bin/env python3
import os 
from os.path import isfile, join
import json
from string import digits
from BitcoinKeyGenerator import BitcoinKeyGenerator
from BitcoinKeySaver import BitcoinKeySaver
import bitcoin


class BitcoinMethodHolder():
    
    def __init__(self, BitcoinKeyChecker, env, searchMethod, methodList):
        self.BitcoinKeyChecker = BitcoinKeyChecker
        self.env = env
        self.searchMethod = searchMethod
        self.methodList = methodList
        print("Bitcoin METHOD HOLDER Created \n")
        
    #gets all binary keys from 0 to one billion
    def one_to_one_billion(self):
        i = 1
        if self.env.ENVIRONMENT == "production":
            amount = 1000000000
        else:
            amount = 100
            
        while i < amount:
            # print(i)
            privateKeyHex = bitcoin.encode_privkey(i, 'hex')
            keyGenerator = BitcoinKeyGenerator(privateKeyHex)
            self.checkKeyGenerator(keyGenerator)
            i = i + 1
            
    def max_minus_one_billion(self):
        max = bitcoin.N
        if self.env.ENVIRONMENT == "production":
            max_minus_one_billion = max - 1000000000
        else:
            max_minus_one_billion = max - 100
            
        i = max
        while i > max_minus_one_billion:
            # print(i)
            privateKeyHex = bitcoin.encode_privkey(1000, 'hex')
            keyGenerator = BitcoinKeyGenerator(privateKeyHex)
            self.checkKeyGenerator(keyGenerator)
            i = i - 1
            
            
            
            
            
            
            
            
            
            
            
            
    def checkIfPrivateKeyIsValid(self, key):
        try:
            check = 0 < key < bitcoin.N
            # print(self.decoded_private_key)
        except Exception as e:
            return False
        if check:
            return True
        else:
            return False
            
            
    def checkKeyGenerator(self, generator):
        # json_data = json.dumps(generator.__dict__)
        # print(json_data)
        # exit()
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
        
        if match1 == True or match2 == True or match3 == True :
            print("MATCH FOUND!!!!!!")
            return True
        else:
            print("not found \n")    
            del generator
            return False
        
    def saveIfMatch(self, match, generator):
        if match:
            print("MATCH FOUND!!!!!!!!!!!!!!!!!!!!!!! ")
            self.saveData(generator)
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
            
    def saveData(self, generator):
        try:
            saver = BitcoinKeySaver()
            saver.setEnv(self.env)
            saver.setGenerator(generator)
            saver.setMethodName(self.searchMethod)
            saver.saveToDatabase() 
        except Exception as e:
            raise
                        