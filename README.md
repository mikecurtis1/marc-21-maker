# marc-21-maker

Python-based MARC21 file builder
Upload a TSV file with book records and generate MARC21 `.mrc` files via a simple web interface. Fully containerized with Flask, Gunicorn, and Nginx.

---

## Installation

```bash
git clone https://github.com/mikecurtis1/marc-21-maker.git
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
