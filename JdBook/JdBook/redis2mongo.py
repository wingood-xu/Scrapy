import redis
from pymongo import MongoClient
import json

redis_cli = redis.Redis(host='localhost',port=6379,db=0)

mongo_cli = MongoClient(host='localhost',port=27017)

mongo_db = mongo_cli['jd_redis']
mongo_col = mongo_db['jd_redis:items']

while True:
    source,data = redis_cli.blpop(['jd_redis:items'])

    str_data = data.decode()
    dict_data = json.loads(str_data)

    mongo_col.insert(dict_data)