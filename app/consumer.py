import redis

with redis.Redis() as redis_client:
    print('random:',redis_client.brpop("queue"))


#redis_client.close()