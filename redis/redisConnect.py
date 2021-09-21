import redis
import time

r = redis.Redis(host='localhost', port=6379, charset="utf-8", decode_responses=True)

# string
print("String")

r.set('index','1')
print('get',r.get('index'))
print('len',r.strlen('index'))

r.incrby('index',23)
print('get',r.get('index'))

r.set('timer','30',4)
time.sleep(2)
print('time to live',r.ttl('timer'))

r.delete('index')

# lists
print("\nList")

a=['a','b','c','d','e']

r.lpush('myList',*a)
print('len',r.llen('myList'))
print('lrange',r.lrange('myList',0,-1))

r.lpop('myList')
print('lrange',r.lrange('myList',0,-1))
print('lindex',r.lindex('myList',2))

r.linsert('myList','before','c','z')
print('lrange',r.lrange('myList',0,-1))

#Hash Map
print("\nHash Map")

data={"name":"Amith","rollno":"10","marks":"50"}
r.hmset('myMap', data)
print('getall',r.hgetall('myMap'))
print('len',r.hlen('myMap'))

print('exists',r.hexists('myMap','rollno'))

r.hdel('myMap','rollno')
print('vals',r.hvals('myMap'))

# Set
print("\nSets")

data1={'a','b','c'}
r.sadd('mySet1',*data1)
print('smembers set1',r.smembers('mySet1'))

data2={'c','d','e'}
r.sadd('mySet2',*data2)

print('sunion',r.sunion('mySet1','mySet2'))
print('sinter',r.sinter('mySet1','mySet2'))
print('sdiff',r.sdiff('mySet1','mySet2'))

r.srem('mySet2','c','d')
print('smembers set2',r.smembers('mySet2'))

r.smove('mySet1','mySet2','c')
print('smembers set2',r.smembers('mySet2'))

# Sorted Set
print('\nSorted Set')

data={'a':10,'b':8,'c':6,'d':4}

r.zadd('mySset',data)
print('zrange',r.zrange('mySset',0,-1))
print('zcard',r.zcard('mySset'))

print('zcount',r.zcount('mySset',1,7))
print('zrank',r.zrank('mySset','c'))
print('zrevrank',r.zrevrank('mySset','c'))
print('zrangebyscore',r.zrangebyscore('mySset',3,9))
