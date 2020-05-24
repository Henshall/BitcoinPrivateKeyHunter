#!/usr/bin/env python3
from app.BitcoinKeyMailer import BitcoinKeyMailer
from app.BitcoinKeyGenerator import BitcoinKeyGenerator
from app.BitcoinKeyChecker import BitcoinKeyChecker

from app.BitcoinMethodHolder import BitcoinMethodHolder
import json
import os
import datetime
import pymysql


class BitcoinMethodStarter():
    
    def __init__(self):
        print("initialized bitcoin finder \n")
        self.env = None
        self.addresses = None
        self.i = 0
        self.methodList = None
        
    
    def setMethodList(self, methodList):
        self.methodList = methodList
    
    def setEnv(self, env):
        self.env = env    
        
    def test(self):
        print("test")
    
    def setAddressList(self, addresses):
        self.addresses = addresses 
        self.BitcoinKeyChecker = BitcoinKeyChecker(addresses)   
    
    def start(self):
        
        self.variableCheck()
        
        dbTest = self.connectToDatabaseTest()
        db = pymysql.connect(self.env.DBHOST,self.env.DBUSER,self.env.DBPASSWORD,self.env.DBNAME)
        cursor = db.cursor()
        sql = "select * from methods"
        
        try:
           # Execute the SQL command
           cursor.execute(sql)
           methodList = cursor.fetchall()
           for data in methodList:
               methodName = data[1]
               status = data[2]
               # ONLY DO SOMETHING IF STATUS IS FALSE
               if status == False or status == 0:
                   #Get Search Method
                   print(methodName)
                   #Run Search Method
                   methodHolder = BitcoinMethodHolder(self.BitcoinKeyChecker, self.env, methodName, self.methodList)
                   function=getattr(methodHolder,methodName)
                   result = function()
                   print("FINISHED " + methodName)
                   if self.env.ENVIRONMENT == "production":
                       sql = "UPDATE methods SET status = 1 WHERE methodName = " + "'" + methodName + "'"
                       try:
                           cursor = db.cursor()
                           cursor.execute(sql)
                           db.commit()
                       except Exception as e:
                           print(e)
                           db.rollback()
                   
        except Exception as e:
           print ("BitcoinFinder Error: unable to fetch data")
           print (e)
        # disconnect from server
        db.close()
            
    
    
    def variableCheck(self):
        if self.addresses == None:
            print("addresses not set --- addresses  check failed in BitcoinFinder variableCheck function")
            print("**********************************************************")
            raise  
        if self.BitcoinKeyChecker == None:
            print("BitcoinKeyChecker not set --- BitcoinKeyChecker  check failed in BitcoinFinder variableCheck function")
            print("**********************************************************")
            raise 
        
        if self.env == None:
            print("env not set --- check failed in BitcoinFinder variableCheck function")
            print("**********************************************************")
            raise    
        if self.env.DBUSER == None:
            print("env.DBUSER not set --- check failed in BitcoinFinder variableCheck function")
            print("**********************************************************")
            raise 
        
        if self.env.DBPASSWORD == None:
            print("env.DBPASSWORD not set --- check failed in BitcoinFinder variableCheck function")
            print("**********************************************************")
            raise  
        
        if self.env.DBHOST == None:
            print("env.DBHOST not set --- check failed in BitcoinFinder variableCheck function")
            print("**********************************************************")
            raise             
        
        if self.env.DBNAME == None:
            print("env.DBNAME not set --- check failed in BitcoinFinder variableCheck function")
            print("**********************************************************")
            raise
    
        
    def connectToDatabaseTest(self):
        try:
            db = pymysql.connect(self.env.DBHOST,self.env.DBUSER,self.env.DBPASSWORD,self.env.DBNAME)
            db.close()
            return True
        except Exception as e:
            try:
                print(e)
                print("PROBLEM CONNECTING TO THE DATABASE WITH THE INPUTS YOU GAVE")
                print("USER = " + self.env.DBUSER)
                print("PASSWORD = " + self.env.DBPASSWORD)
                print("HOST = " + self.env.DBHOST)
                print("DBNAME = " + self.env.DBNAME)
            except Exception as e:
                print(e)
                raise
            return False
    
