#!/usr/bin/env python3
import bitcoin
import numpy as np
import sys

class BitcoinKeyGenerator():
    
    def __init__(self, PrivateKey = None):
        if PrivateKey == None:
            print("THERE WAS NO PRIVATE KEY GIVEN AS ARGUMENT \n")
            raise
        else:
            self.private_key = PrivateKey
        try:
            self.decoded_private_key = bitcoin.decode_privkey(self.private_key, 'hex')
        except Exception as e:
            pass  
          #creates decimal of private key  - this function turns it into either decimal or hex
        check = self.checkIfPrivateKeyIsValid();
        if check:
            print("Valid Private Key \n")
            self.wif_encoded_private_key = bitcoin.encode_privkey(self.decoded_private_key, 'wif')
            # GENERATE PUBLIC KEYS
            self.public_key = bitcoin.privkey_to_pubkey(self.private_key) # located in files
            # self.bitcoinAddress = bitcoin.pubkey_to_address(self.public_key)
            # 
            # 
            # 
            # self.public_key_f_m = bitcoin.fast_multiply(bitcoin.G, self.decoded_private_key)
            # self.hex_encoded_public_key = bitcoin.encode_pubkey(self.public_key_f_m, 'hex')    
            # 
            # self.hex_compressed_public_key = self.generateHexCompressedPublicKey(self.public_key_f_m)
            # self.bitcoinAddress2 = bitcoin.pubkey_to_address(self.public_key_f_m)
            # self.compressedBitcoinAddress = bitcoin.pubkey_to_address(self.hex_compressed_public_key.encode('utf-8'))
            
        else:
            print("Invalid Private Key Check Failed!!!\n")
        
    
    def checkIfPrivateKeyIsValid(self):
        try:
            check = 0 < self.decoded_private_key < bitcoin.N
            # print(self.decoded_private_key)
        except Exception as e:
            return False
        if check:
            return True
        else:
            return False
    
    def generateHexCompressedPublicKey(self, public_key):
        (public_key_x, public_key_y) = public_key
        if public_key_y % 2 == 0:
          compressed_prefix = '02'
        else:
          compressed_prefix = '03'
        return compressed_prefix + bitcoin.encode(public_key_x, 16)
           
    def generateRandomPrivateKey(self):    
        return bitcoin.random_key()  
