FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install jpegoptim

# Requirements have to be pulled and installed here, otherwise caching won't work
COPY ./requirements/production.txt /requirements.txt

WORKDIR /app
COPY . /app

RUN pip install -r /requirements.txt \
    && groupadd -r django \
    && useradd -r -g django django --uid 1000

RUN chown -R django /app

COPY ./docker_compose/django/production/start.sh /start.sh
COPY ./docker_compose/django/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r//' /entrypoint.sh \
    && sed -i 's/\r//' /start.sh \
    && chmod +x /entrypoint.sh \
    && chown django /entrypoint.sh \
    && chmod +x /start.sh \
    && chown django /start.sh

ENTRYPOINT ["/entrypoint.sh"]
