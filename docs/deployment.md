# Deployment Guide

## Prerequisites

* Docker
* Docker Compose
* Git
* Ubuntu Server

## Clone Repository

```bash
git clone <repository-url>
cd fastapi-devops-production-deployment
```

## Configure Environment Variables

```bash
cp .env.example .env
```

## Build and Start Application

```bash
docker compose up -d --build
```

## Verify Services

```bash
docker ps
```

## Verify Application

```bash
curl http://localhost/health
```

Expected Output:

```json
{
  "status": "healthy"
}
```
