import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["learnDB"]

mycol = mydb["employees"]

data = [
        {
            "_id":1,
            "jobTitleName":"Developer",
            "firstName":"Amith",
            "lastName":"J",
            "employeeCode":"E1",
            "region":"BR",
            "lang":["ML","EN"],
            "marks":[50,60,70],
            "address":{
                "street":"Madathil",
                "city":"Muvattupuzha",
                "state":"Kerala",
                "PIN":"686661",
            },
            "emailAddress":"amithj@email.com"
        },
        {
            "_id":2,
            "jobTitleName":"Manager",
            "firstName":"Akhil",
            "lastName":"M D",
            "employeeCode":"E2",
            "region":"BR",
            "lang":["EN","HN"],
            "marks":[75,78,80],
            "address":{
                "street":"Mundakkal",
                "city":"Vadakkanchery",
                "state":"Kerala",
                "PIN":"686678",
            },
            "emailAddress":"akhilmd@email.com"
        },
        {
            "_id":3,
            "jobTitleName":"HR",
            "firstName":"Abil",
            "lastName":"Das",
            "employeeCode":"E3",
            "region":"KL",
            "lang":["ML","EN","HN"],
            "marks":[90,45,85],
            "address":{
                "street":"Animootil",
                "city":"Anicadu",
                "state":"Kerala",
                "PIN":"686661",
            },
            "emailAddress":"abildas@email.com"
        }
        ]

mycol.insert_many(data)
mycol.update_many({"firstName":"Akhil"},{"$set":{"firstName":"Binoy","lastName":"George"}})

x = mycol.find({"$or":[{"firstName":{"$regex":"^A"}},{"firstName":{"$regex":"^B"}}]},{"firstName":1})
for i in x:
    print(i)

print()

x = mycol.find({"lang":{"$all":["EN","ML"]}},{"firstName":1,"lang":1})
for i in x:
    print(i)

print()

x = mycol.find({"address.state":"Kerala","address.PIN":"686661"})
for i in x:
    print(i['address'])

print()

x = mycol.find({"marks":{"$elemMatch":{"$gte":80,"$lt":90}}})
for i in x:
    print(i['marks'])

print()

mycol.delete_many({"region":"KL"})
x =  mycol.find()
for i in x:
    print(i)

    