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

## SSL Setup Approach

SSL is not currently enabled because a production domain name is not available.

For a production deployment:

1. Point a domain name to the EC2 Elastic IP using a DNS A record.
2. Install Certbot on the EC2 server.
3. Generate a free Let's Encrypt SSL certificate.
4. Configure NGINX to serve HTTPS on port 443.
5. Redirect all HTTP traffic from port 80 to HTTPS.
6. Configure automatic certificate renewal.

The current AWS Security Group already allows HTTPS traffic on port 443.
## Basic Server Security Measures

- SSH access uses key-based authentication.
- AWS Security Groups restrict inbound traffic.
- Only ports 22, 80, and 443 are allowed as required.
- PostgreSQL port 5432 is not exposed publicly.
- Redis port 6379 is not exposed publicly.
- Application secrets are stored in the `.env` file and GitHub Actions Secrets.
- The `.env` file is excluded from Git using `.gitignore`.
- Docker services use restart policies for reliability.
- NGINX is used as the public reverse proxy, while backend services remain inside the Docker Compose network.



