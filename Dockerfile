FROM python:3.11-slim

WORKDIR /app

COPY app/ /app/

RUN pip install --no-cache-dir flask gunicorn

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
