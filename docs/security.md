# Security Measures

## Environment Variables

Sensitive values are stored in .env files and are not committed to GitHub.

## Firewall

Only required ports should be opened:

* 22 (SSH)
* 80 (HTTP)
* 443 (HTTPS)

Example:

```bash
sudo ufw allow 22
sudo ufw allow 80
sudo ufw allow 443
sudo ufw enable
```

## SSL

SSL certificates can be configured using Let's Encrypt and Certbot.

```bash
sudo certbot --nginx
```

## Fail2Ban

Protect against brute-force attacks.

```bash
sudo apt install fail2ban
```
