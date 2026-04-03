# marc-21-maker
Marc-21-maker is a lightweight Python project for generating valid MARC 21 binary records from structured input.

---

## Installation

```bash
git clone
```

Build and start containers

```bash
docker-compose up --build
```

Nginx logs

```bash
docker-compose exec nginx tail -f /var/log/nginx/access.log
```

Flask/Gunicorn logs

```bash
docker-compose logs -f app
```

Run app in browser

[http://localhost:8080](http://localhost:8080)
