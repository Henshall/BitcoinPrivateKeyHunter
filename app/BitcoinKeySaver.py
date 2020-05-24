#!/usr/bin/env python3
import env
import json
import pymysql


class BitcoinKeySaver():
    """docstring for BitcoinKeyMailer."""

    def __init__(self):        
        print("***************************")
        self.env = None 
        self.generator = None 
        self.methodName = None
    
        
    def setEnv(self, env):        
        self.env = env
    
    def setMethodName(self, methodName):        
        self.methodName = methodName    
        
    def setGenerator(self, generator):        
        self.generator = generator
        
    def setMethodList(self, methodList):
        self.methodList = methodList   
        
    def setMethodName(self, methodName):
        self.methodName = methodName        
        
    def saveToTextFile(self):
        fl = open(env.KEYS_FOUND_TEXT_FILE_NAME, "a")
        fl.write("FOUND SOMETHING INTERESTING \n")
        fl.write("KEY INFO = " + self.generator + "\n")
        fl.write("NOTE: PUBLIC KEY MAY NEED TO BE ALL UPPER CASE")
        fl.close()
        
    def saveToDatabase(self):    
        # Open database connection
        db = pymysql.connect(env.DBHOST,env.DBUSER,env.DBPASSWORD,env.DBNAME)
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        generator_data = json.dumps(self.generator.__dict__)
        # Prepare SQL query to INSERT a record into the database.
        sql = "INSERT INTO bitcoin_keys(method_id,bitcoin_keys) VALUES (" + "2" + ", " +"'" + generator_data + "'" + ")"     
        try:
           # Execute the SQL command
           cursor.execute(sql)
           # Commit your changes in the database
           db.commit()
        except Exception as e:
            print(e)
           # Rollback in case there is any error
            db.rollback()
        # disconnect from server
        db.close()
        
    
        
    