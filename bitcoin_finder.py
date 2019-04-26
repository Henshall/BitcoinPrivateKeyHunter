#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Infomation: Script to brute bitcoin addresses
# often the script will stop running, so I have set it up with a cron job which executes it every minute.

from bit import Key
import os
import json
import time
import ecdsa
import hashlib
import requests
import binascii
import sys
import smtplib
import time
import addresses
import env

def send(pub, pri, address, amount):
        text = env.email_text + "\n PUBLIC KEY = " + pub + "\n PRIVATE KEY = " + pri + "\n ADDRESS = " + address
        server = smtplib.SMTP(env.SMTP_HOST, env.SMTP_PORT)
        server.ehlo()
        server.starttls()
        server.login(env.USER, env.PASS)
        server.sendmail(env.SEND_FROM, env.SEND_TO, text)
        server.close()
        print('Email sent!')

def prikey():
    return binascii.hexlify(os.urandom(32)).decode('utf-8')

def pubkey(prikey):
    prikey = binascii.unhexlify(prikey)
    sign = ecdsa.SigningKey.from_string(prikey, curve=ecdsa.SECP256k1)
    return '04' + binascii.hexlify(
        sign.verifying_key.to_string()).decode('utf-8')

def address(pubkey):
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    ares = '0'
    byte = '00'
    zero = 0
    val = hashlib.new('ripemd160')
    val.update(hashlib.sha256(binascii.unhexlify(pubkey.encode())).digest())
    cim = (byte + val.hexdigest())
    doublehash = hashlib.sha256(
        hashlib.sha256(binascii.unhexlify(cim.encode())).digest()).hexdigest()
    address = cim + doublehash[0:8]
    for char in address:
        if (char != ares):
            break
        zero += 1
    zero = zero // 2
    nom = int(address, 16)
    result = []
    while (nom > 0):
        nom, reder = divmod(nom, 58)
        result.append(alphabet[reder])
    count = 0
    while (count < zero):
        result.append(alphabet[0])
        count += 1
    return ''.join(result[::-1])

def main():
    fl = open(env.KEYS_FOUND_TEXT_FILE_NAME, "a")
    fl.write("THIS IS THE TEST")
    fl.close()
    i = 0
    data = [0, 0, 0]
    while i < 9000000:
        data[0] = prikey()
        data[1] = pubkey(data[0])
        data[2] = address(data[1])
        data[2] ="1BamMXZBPLMwBT3UdyAAKy3ctGDbXNKoXk"

        datas = (
            "\nAddress: " + str(data[2]) + "\n" + "Private Key: " +
            str(data[0]) + "\n" + "Wallet Import Format Private Key: " +
            str(Key.from_hex(data[0]).to_wif()) + "\n" + "Public Key: " + str(
                data[1]).upper() + "\n" )

        for item in addresses.addresses:        # Second Example
            i = i + 1
            if data[2] == item:
                print("FOUND SOMETHING INTERESTING")
                print("PUBLIC KEY = " + data[1])
                print("PRIVATE KEY = " + data[0])
                print("ADDRESS = " + data[2])
                print(datas)
                send(data[0], data[1], data[2], "some amount")
                # fl = open(env.KEYS_FOUND_TEXT_FILE_NAME, "a")
                # fl.write(datas)
                # fl.close()



if __name__ == '__main__':
    print("\n-----------------BITCOIN FINDER STARTED---------------!")
    main()
