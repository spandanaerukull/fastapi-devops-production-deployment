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

 ## Backup and Restart Strategy

### PostgreSQL Backup

Create a database backup:

```bash
docker compose exec -T postgres \
pg_dump -U fastapiuser fastapidb > backup.sql
```

Restore a database backup:

```bash
cat backup.sql | docker compose exec -T postgres \
psql -U fastapiuser fastapidb
```

### Restart Strategy

All services use Docker restart policies so they restart automatically after a container failure or server reboot.

To restart all services manually:

```bash
docker compose restart
```

To rebuild and restart after a deployment:

```bash
docker compose up -d --build --remove-orphans
```

To check service status:

```bash
docker compose ps
```

Application health can be verified using:

```bash
curl http://localhost/health
curl http://localhost/db-check
curl http://localhost/redis-check
```

## Logging Strategy

The FastAPI application uses Python's built-in logging module to record application startup, endpoint access, successful service connections, and errors.

Application logs can be viewed using:

```bash
docker compose logs --tail=100 fastapi
```

NGINX access and error logs can be viewed using:

```bash
docker compose logs --tail=100 nginx
```

PostgreSQL and Redis logs can be viewed using:

```bash
docker compose logs --tail=100 postgres
docker compose logs --tail=100 redis
```

To follow all container logs in real time:

```bash
docker compose logs -f
```

Docker log rotation should be configured in production to prevent logs from consuming excessive disk space.

## Deployment Instructions

### 1. Launch an EC2 Server

Create an Ubuntu EC2 instance and configure the Security Group with:

* Port 22 for SSH
* Port 80 for HTTP
* Port 443 for HTTPS

PostgreSQL port `5432` and Redis port `6379` must not be exposed publicly.

### 2. Connect to the Server

```bash
ssh -i your-key.pem ubuntu@18.213.165.227
```

### 3. Install Required Tools

Install Git, Docker, and Docker Compose on the server.

Verify the installations:

```bash
git --version
docker --version
docker compose version
```

### 4. Clone the Repository

```bash
git clone https://github.com/spandanaerukulla/fastapi-devops-production-deployment.git
cd fastapi-devops-production-deployment
```

### 5. Create the Environment File

Copy the example environment file:

```bash
cp .env.example .env
```

Update `.env` with secure production values before starting the services.

### 6. Start the Application

```bash
docker compose up -d --build
```

### 7. Verify the Containers

```bash
docker compose ps
```

The following services should be running:

1. FastAPI
2. PostgreSQL
3. Redis
4. NGINX

### 8. Verify the Endpoints

```bash
curl http://localhost/health
curl http://localhost/db-check
curl http://localhost/redis-check
```

### 9. Access the Application

Open the following URLs using the EC2 Elastic IP:

```text
http://18.213.165.227/
http://18.213.165.227/health
http://18.213.165.227/db-check
http://18.213.165.227/redis-check
http://18.213.165.227/docs
```

### 10. Automatic Deployment

Every push to the `master` branch triggers the GitHub Actions workflow.

The workflow:

1. Builds the Docker image.
2. Connects to the EC2 server using SSH.
3. Pulls the latest source code.
4. Rebuilds and restarts the Docker Compose services.
5. Verifies the health, database, and Redis endpoints.
