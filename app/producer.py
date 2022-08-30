import redis
import random
with redis.Redis() as redis_client:
    redis_client.lpush("queue",random.randint(0,100))


#redis_client.close()