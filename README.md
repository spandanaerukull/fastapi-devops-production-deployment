# FastAPI DevOps Production Deployment

## Project Overview

This project demonstrates a production-ready deployment of a FastAPI application using Docker, Docker Compose, PostgreSQL, Redis, NGINX Reverse Proxy, and GitHub Actions CI/CD.

## Architecture
Developer
   |
   | git push
   v
GitHub Repository
   |
   | GitHub Actions CI/CD
   v
AWS EC2 / Elastic IP
   |
   v
NGINX Reverse Proxy
   |
   v
FastAPI Application
   |             |
   v             v
PostgreSQL      Redis


PostgreSQL and Redis are accessible only within the Docker Compose internal network and are not exposed publicly.


## Technology Stack

* FastAPI
* PostgreSQL
* Redis
* Docker
* Docker Compose
* NGINX
* GitHub Actions

## Features

* Containerized application
* PostgreSQL database integration
* Redis caching integration
* NGINX reverse proxy
* Health check endpoint
* Environment variable configuration
* CI/CD deployment pipeline
* Backup and recovery strategy
* Security best practices

## Application Endpoints

| Endpoint     | Purpose               |
| ------------ | --------------------- |
| /            | Home                  |
| /health      | Health Check          |
| /db-check    | Database Connectivity |
| /redis-check | Redis Connectivity    |

## Run Locally

```bash
docker compose up -d --build
```

## Stop Application

```bash
docker compose down
```

## Health Check

```bash
http://localhost/health
```
Test automatic EC2 deployment
