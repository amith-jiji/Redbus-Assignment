import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["learnDB"]

mycol = mydb["students"]

def insertData():
    id = list(mycol.find().sort("_id",-1))[0]['_id']
    name = input("Enter Name : ")
    exam = float(input("Enter Exam Score : "))
    quiz = float(input("Enter Quiz Score : "))
    hw = float(input("Enter Homework Score : "))
    mycol.insert_one({"_id":id+1,"name":name,"score":[{"score":exam,"type":"exam"},{"score":quiz,"type":"quiz"},{"score":hw,"type":"homework"}]})
    print("ID no is",id+1)

def findData():
    id = int(input("Enter ID : "))
    result = mycol.find_one({"_id":id})
    if result:
        print(result)
    else:
        print("Item not found")

def deleteData():
    id = int(input("Enter ID : "))
    x = mycol.delete_one({"_id":id})
    if x.deleted_count:
        print("Deletion Succesful")
    else:
        print("Deletion Unsuccesful")

def updateData():
    _id = int(input("Enter ID : "))
    name = input("Enter New Name : ")
    exam = float(input("Enter New Exam Score : "))
    quiz = float(input("Enter New Quiz Score : "))
    hw = float(input("Enter New Homework Score : "))
    x=mycol.update_one({"_id":_id},{"$set":{"name":name,"score":[{"score":exam,"type":"exam"},{"score":quiz,"type":"quiz"},{"score":hw,"type":"homework"}]}})
    if x.modified_count:
        print("Updation Sucessfull")
    else:
        print("Updation Unsuccesfull")

if __name__=="__main__":
    while(True):
        print("1.Enter Data\n2.Find Data\n3.Update Data\n4.Delete Data\n5.Exit\n")
        c = int(input())
        if c==1:
            insertData()
        elif c==2:
            findData()
        elif c==3:
            updateData()
        elif c==4:
            deleteData()
        else:
            break
        print()
            




    

