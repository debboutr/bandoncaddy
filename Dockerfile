FROM python:3.13.5-bullseye

ENV TZ="America/Los_Angeles"

WORKDIR /app

ADD . /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt

ENV STATIC_ROOT /vol/static
CMD ["/app/entrypoint.sh"]
