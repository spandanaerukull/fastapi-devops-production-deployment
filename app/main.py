import logging

logging.basicConfig(
    filename='logs/app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Application Started")
from fastapi import FastAPI
import os
import psycopg2
import redis

app = FastAPI(title="DevOps Production FastAPI App")

DB_HOST = os.getenv("DB_HOST", "postgres")
DB_NAME = os.getenv("DB_NAME", "appdb")
DB_USER = os.getenv("DB_USER", "appuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "apppassword")

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))


@app.get("/")
def home():
    return {
        "message": "FastAPI DevOps Production Deployment Project",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/db-check")
def db_check():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        conn.close()
        return {"database": "connected"}
    except Exception as e:
        return {"database": "connection_failed", "error": str(e)}


@app.get("/redis-check")
def redis_check():
    try:
        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
        r.set("app_status", "redis_connected")
        value = r.get("app_status")
        return {"redis": value}
    except Exception as e:
        return {"redis": "connection_failed", "error": str(e)}
    
    import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logging.info("Application Started")