import pymongo
import redis
import mysql.connector
import time

myConnection = mysql.connector.connect(host="localhost",port=3306,user="root",passwd="bindupayyala",database="studdb")

r = redis.Redis(host='localhost', port=6379, charset="utf-8", decode_responses=True)

myCursor  = myConnection.cursor()

rstart = time.perf_counter()
redisVal = r.hget('insurance','construction')
relapsed = time.perf_counter() - rstart
print("Redis",redisVal,relapsed)

mstart = time.perf_counter()
myCursor.execute("SELECT construction FROM insurance WHERE policyID = 398149")
sqlVal = myCursor.fetchall()[0][0]
melapsed = time.perf_counter() - mstart
print("Mysql",sqlVal,melapsed)