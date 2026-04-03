# marc-21-maker

[![Python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/flask-3.0-green.svg)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/docker-29.2-blue.svg)](https://www.docker.com/)

Python-based MARC 21 ([ISO 2709](https://www.iso.org/standard/41319.html)) file builder.

Upload a TSV file with book records and generate MARC 21 `.mrc` files via a simple web interface. Fully containerized with Flask, Gunicorn, and Nginx.

---

## Features

* Convert TSV or CSV metadata into MARC 21 format
* Web interface using Flask templates
* Fully containerized for production-like deployment:
  * Gunicorn for WSGI app serving
  * Nginx reverse proxy
* Integrated logging for both Nginx and Flask/Gunicorn
* Easy local testing and Docker Compose setup

---

## Project Structure

```text
marc-21-maker/
├─ nginx/
│  ├─ default.conf        # Nginx configuration
│  └─ logs/               # Access and error logs
├─ app/
│  ├─ app.py              # Flask application
│  ├─ marc21.py           # MARC21Maker class
│  ├─ escape_string.py    # Escape string helper
│  ├─ templates/
│  │  └─ form.html        # Upload form template
│  └─ data/
│     └─ books.tsv        # Sample TSV input
├─ Dockerfile
├─ requirements.txt
└─ docker-compose.yml
```

---

## Prerequisites

* Docker
* Docker Compose

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

---

## Usage

Run app in browser

[http://localhost:8080](http://localhost:8080)

Upload a TSV or CSV file (demo file included in the repo)

```text
L5  L6  L7  number  author        title       pubdate
n   a   m   0001    John Doe      Title #1   2024
n   a   m   0002    Jane Doe      Title #2   2025
n   a   m   0003    John Q Public Title #3   2026
```

## License

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

This project is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.

---
