FROM python:3.6

ARG ENVIRONMENT=production

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install jpegoptim

# Requirements have to be pulled and installed here, otherwise caching won't work
COPY ./requirements/${ENVIRONMENT}.txt /requirements.txt

RUN mkdir -p /app/static
WORKDIR /app
COPY . .

COPY ./docker_compose/wait-for-it.sh /bin/wait-for-it
RUN chmod +x /bin/wait-for-it

RUN pip install -r /requirements.txt \
    && groupadd -r django \
    && useradd -r -g django django --uid 1000

COPY ./docker_compose/django/${ENVIRONMENT}/start.sh /start.sh
RUN sed -i 's/\r$//g' /start.sh \
    && chmod +x /start.sh \
    && chown django /start.sh

RUN chown -R django /app

EXPOSE 8000

USER django

CMD ["/start.sh"]
