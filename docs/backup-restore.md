# Backup and Restore Strategy

## PostgreSQL Backup

```bash
docker exec postgres_db pg_dump -U appuser appdb > backup.sql
```

## Restore Database

```bash
cat backup.sql | docker exec -i postgres_db psql -U appuser appdb
```

## Automated Backup

A cron job can be scheduled:

```bash
0 1 * * * backup.sh
```

## Container Recovery

Docker Compose restart policy:

```yaml
restart: always
```

ensures automatic recovery after server reboot or container failure.
