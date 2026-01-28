FROM python:3.13-slim

ENV TZ=America/Los_Angeles

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt

ENV STATIC_ROOT /vol/static
CMD ["/app/entrypoint.sh"]
