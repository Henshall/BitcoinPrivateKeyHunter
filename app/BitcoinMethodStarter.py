#!/usr/bin/env python3
from app.BitcoinKeyMailer import BitcoinKeyMailer
from app.BitcoinKeyGenerator import BitcoinKeyGenerator
from app.BitcoinKeyChecker import BitcoinKeyChecker
from app.BitcoinMethodHolder import BitcoinMethodHolder
import pymysql


class BitcoinMethodStarter():
    
    def __init__(self):
        print("initialized bitcoin finder \n")
        self.env = None
        self.addresses = None
        self.i = 0

    def setEnv(self, env):
        self.env = env    
        
    def test(self):
        print("test")
    
    def setAddressList(self, addresses):
        self.addresses = addresses 
        self.BitcoinKeyChecker = BitcoinKeyChecker(addresses)   
    
    def start(self):
        self.variableCheck()
        self.connectToDatabaseTest()
        methodTable = self.getMethodTableFromDatabase()
        try:
           for data in methodTable:
               methodName = data[1]
               status = data[2]
               # ONLY RUN METHOD IF IT HASNT BEEN RUN BEFORE
               if status == False or status == 0:
                   print(methodName)
                   self.BitcoinKeyChecker.setSearchMethod(methodName)
                   #Run Search Method
                   methodHolder = BitcoinMethodHolder(self.BitcoinKeyChecker, self.env, methodName)
                   function=getattr(methodHolder,methodName)
                   result = function()
                   print("FINISHED " + methodName)
                   if self.env.ENVIRONMENT == "production":
                       self.updateMethodStatusInDatabase(methodName)
        except Exception as e:
           print ("BitcoinMethodStarter Error: unable to fetch data")
           print (e)
        db.close()
            
    def getMethodTableFromDatabase(self):
        db = pymysql.connect(self.env.DBHOST,self.env.DBUSER,self.env.DBPASSWORD,self.env.DBNAME)
        cursor = db.cursor()
        sql = "select * from methods"
        cursor.execute(sql)
        return cursor.fetchall()
        
    def updateMethodStatusInDatabase(self,methodName):
        sql = "UPDATE methods SET status = 1 WHERE methodName = " + "'" + methodName + "'"
        try:
            db = pymysql.connect(self.env.DBHOST,self.env.DBUSER,self.env.DBPASSWORD,self.env.DBNAME)
            cursor = db.cursor()
            cursor.execute(sql)
            db.commit()
            db.close()
        except Exception as e:
            print(e)
            db.rollback()
            db.close()
    
    def variableCheck(self):
        if self.addresses == None or self.BitcoinKeyChecker == None or self.env == None or self.env.DBUSER == None or self.env.DBPASSWORD == None or self.env.DBHOST == None or self.env.DBNAME == None:
            print("This will throw an error automatically if one of the following variables is undefined")
            raise
        return True    
            
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
    