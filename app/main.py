from fastapi import FastAPI
import requests
import typing
import random
import redis
app = FastAPI()


r = redis.Redis(
    host='redis',
    port=6379)

@app.get("/")
async def read_main():
    r.set('name','Dauren Shalabayev')
    value = r.get('name')
    return {"Hello": value}

@app.get("/producer")
async def producer():
    with r as redis_client:
        for i in range(10):
            redis_client.lpush("queue",i)
            
        return {'Start'}

@app.get("/consumer")
async def consumer():
    with r as redis_client:
        return {redis_client.brpop("queue")}
