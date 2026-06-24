
import logging
import os

from fastapi import FastAPI
import psycopg2
import redis

# ==========================================================
# Logging Configuration
# ==========================================================

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

logger.info("Application Started")

# ==========================================================
# FastAPI Application
# ==========================================================

app = FastAPI(title="DevOps Production FastAPI App")

# ==========================================================
# Environment Variables
# ==========================================================

DB_HOST = os.getenv("DB_HOST", "postgres")
DB_NAME = os.getenv("DB_NAME", "appdb")
DB_USER = os.getenv("DB_USER", "appuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "apppassword")

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

# ==========================================================
# Home Endpoint
# ==========================================================

@app.get("/")
def home():
    logger.info("Home endpoint called")

    return {
        "message": "FastAPI DevOps Production Deployment Project",
        "status": "running"
    }

# ==========================================================
# Health Check Endpoint
# ==========================================================

@app.get("/health")
def health_check():
    logger.info("Health endpoint called")

    return {
        "status": "healthy"
    }

# ==========================================================
# PostgreSQL Connectivity Check
# ==========================================================

@app.get("/db-check")
def db_check():

    logger.info("Database endpoint called")

    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )

        conn.close()

        logger.info("Database connection successful")

        return {
            "database": "connected"
        }

    except Exception as e:

        logger.error(f"Database connection failed: {str(e)}")

        return {
            "database": "connection_failed",
            "error": str(e)
        }

# ==========================================================
# Redis Connectivity Check
# ==========================================================

@app.get("/redis-check")
def redis_check():

    logger.info("Redis endpoint called")

    try:
        r = redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            decode_responses=True
        )

        r.set("app_status", "redis_connected")

        value = r.get("app_status")

        logger.info("Redis connection successful")

        return {
            "redis": value
        }

    except Exception as e:

        logger.error(f"Redis connection failed: {str(e)}")

        return {
            "redis": "connection_failed",
            "error": str(e)
        }
