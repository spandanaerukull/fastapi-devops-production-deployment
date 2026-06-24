# Architecture Diagram

```
                Internet
                    |
                    v
             +-------------+
             |    NGINX    |
             +-------------+
                    |
                    v
             +-------------+
             |   FastAPI   |
             +-------------+
               |         |
               v         v
        +---------+  +---------+
        | PostgreSQL| | Redis |
        +---------+  +---------+
```

Deployment:
Docker Compose manages all containers.

CI/CD:
GitHub → GitHub Actions → Docker Build → Server Deployment
