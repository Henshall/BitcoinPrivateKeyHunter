#!/usr/bin/env python3
import os 
from os.path import isfile, join
import json
from string import digits
import bitcoin
import math
import time
import decimal
from mpmath import *


class BitcoinMethodHolder():
    
    def __init__(self, BitcoinKeyChecker, env, searchMethod, methodList):    
        self.BitcoinKeyChecker = BitcoinKeyChecker
        self.env = env
        self.searchMethod = searchMethod
        self.methodList = methodList
        self.numbersList = []
        print("Bitcoin METHOD HOLDER Created \n")
        
    #gets all binary keys from 0 to one billion
    def one_to_one_billion(self):
        print("starting one_to_one_billion \n")
        if self.env.ENVIRONMENT == "production":
            amount = 1000000001
        else:
            amount = 3
        i = 1
        while i < amount:
            # print(i)
            self.BitcoinKeyChecker.checkBitcoinGeneratorFromInteger(i)
            # check additional
            if i > 900000000:
                self.loopNumberCheck( "multiply", i, 1, 11)
                self.loopNumberCheck( "exponent", i, 1, 100)
            if i < 1000001:
                self.loopNumberCheck( "bit_shift_left", i, 1, 40)
                self.loopNumberCheck( "bit_shift_right", i, 1, 40)
            i = i + 1

    def max_minus_one_billion(self):
        print("starting max_minus_one_billion \n")
        max = bitcoin.N
        if self.env.ENVIRONMENT == "production":
            max_minus_one_billion = max - 1000000000
        else:
            max_minus_one_billion = max - 5
        i = max - 1
        while i > max_minus_one_billion:
            print(i)
            self.BitcoinKeyChecker.checkBitcoinGeneratorFromInteger(i)
            # self.loopNumberCheck( "root", i, 1, 1)
            i = i - 1
                
    def to_max_all_powers(self):
        # here we loop through all the powers starting with 2. 
        # 2 * 2 until the max number, then 3 * 3 until the max number etc.
        print("starting to_max_all_powers \n")
        if self.env.ENVIRONMENT == "production":
            mainLoopAmount = 1001
            subLoopAmount = 101
        else:
            mainLoopAmount = 4
            subLoopAmount = 2
        i = 2
        j = 1
        while i < mainLoopAmount:
            while j < bitcoin.N:
                j = j * i
                self.loopNumberCheck( "bit_shift_left", j, 1, subLoopAmount)
                self.loopNumberCheck( "add", j, 10, subLoopAmount)
                self.loopNumberCheck( "subtract", j, 10, subLoopAmount)
                self.loopNumberCheck( "multiply", j, 1, subLoopAmount)
                self.loopNumberCheck( "divide", j, 1, subLoopAmount)
                self.loopNumberCheck( "root", j, 1, subLoopAmount)
            i = i + 1    
            j = 1          
    
    
    def to_max_all_multiples_of_ten(self):
        # loops through 1 to one million and multiples each 
        # number by ten until max and then guesses that number
        print("starting to_max_all_powers \n")
        if self.env.ENVIRONMENT == "testing":
            mainLoopAmount = 1000001
            subLoopAmount = 10
        else:
            mainLoopAmount = 4
            subLoopAmount = 1
        i = 1
        j = 1
        #1 - one one million
        while i < mainLoopAmount:
            while j < bitcoin.N:
                numberToCheck = i * j
                try:
                    self.BitcoinKeyChecker.checkBitcoinGeneratorFromInteger(int(numberToCheck))
                except Exception as e:
                    pass
                j = j * 10
            i = i + 1
            j = 1  
        
             
            
    # def all_interesting_numbers(self):
    #     print("starting all_interesting_numbers \n")
    #     if self.env.ENVIRONMENT == "production":
    #         amount = bitcoin.N
    #     else:
    #         amount = 10
    # 
    #     interestingNumbers = self.interestingNumbers()
    #     for number in interestingNumbers:    
    #         self.loopNumberCheck( "bit_shift_left", number, 1, 1001)
    #         self.loopNumberCheck( "bit_shift_right", number, 1, 1001)
    #         self.loopNumberCheck( "add", number, 10, 1001)
    #         self.loopNumberCheck( "subtract", number, 10, 1001)
    #         self.loopNumberCheck( "multiply", number, 1, 1001)
    #         self.loopNumberCheck( "divide", number, 1, 1001)
    # 
            # self.loopNumberCheck( "root", number, 1, 101)
        
    def loopNumberCheck(self, type, number, increaseAmount, loopAmount):
        i = 0
        j = 0
        while j < loopAmount:
            print("j = " + str(j))
            print("i = " + str(i))
            print("type = " + str(type))
            print("increaseAmount = " + str(increaseAmount))
            
            if type == "add":
                numberToCheck = number + i
            elif type == "subtract":
                numberToCheck = number - i    
            elif type == "multiply":
                # without this library you cannot effectively multiply numbers
                mp.dps = 200; mp.pretty = True
                numberToCheck = fmul(number, i, exact=True)
            elif type == "divide":
                if i == 0:
                    numberToCheck = number
                else:
                    # without this library you cannot effectively divide numbers
                    mp.dps = 200; mp.pretty = True
                    numberToCheck = fdiv(number, i)
            elif type == "exponent":
                mp.dps = 200; mp.pretty = True
                numberToCheck = power(number, i)
            elif type == "root":
                if i == 0:
                    numberToCheck = number
                else:
                    mp.dps = 200; mp.pretty = True
                    numberToCheck = root(number, i) 
            elif type == "bit_shift_left":
                numberToCheck = number << i
            elif type == "bit_shift_right":
                numberToCheck = number >> i    
            #NOW WE CAN CHECK THE NUMBER AND SEE IF WE FOUND A KEY    
            print("numberToCheck = " + str(int(numberToCheck)))
            # if j == 10:
            #     exit()
            
            try:
                self.BitcoinKeyChecker.checkBitcoinGeneratorFromInteger(int(numberToCheck))
            except Exception as e:
                pass      
            i = i + increaseAmount
            j = j + 1
        return True    
            
            
    def interestingNumbers(self):
        return [
            115792089237316195423570985008687907852837564279074904382605163141518161494337,
            314159265358979323846264338327950288419716939937510582097494459230781640628620, #pi
            271828182845904523536028747135266249775724709369995957496696762772407663035354, #e
            161803398874989484820458683436563811772030917980576286213544862270526046281890, # golden ratio
            141421356237309504880168872420969807856967187537694807317667973799073247846210, # square root of 2
            173205080756887729352744634150587236694280525381038062805580697945193301690880, # square root of 3
            223606797749978969640917366873127623544061835961152572427089724541052092563780, # square root of 5
            264575131106459059050161575363926042571025918308245018036833445920106882323028, # square root of 7
            282842712474619009760337744841939615713934375075389614635335947598146495692421, # square root of 8
        ]
                            