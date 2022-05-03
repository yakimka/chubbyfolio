FROM python:3.9

ARG ENVIRONMENT=production

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install jpegoptim

# Requirements have to be pulled and installed here, otherwise caching won't work
COPY ./backend/requirements/${ENVIRONMENT}.txt /requirements.txt
RUN pip install -r /requirements.txt \
    && groupadd -r django \
    && useradd -r -g django django --uid 1000

WORKDIR /app
COPY ./backend .

COPY ./docker_compose/wait-for-it.sh /bin/wait-for-it
RUN chmod +x /bin/wait-for-it

COPY ./docker_compose/django/${ENVIRONMENT}/start.sh /start.sh
RUN sed -i 's/\r$//g' /start.sh \
    && chmod +x /start.sh \
    && chown django /start.sh

COPY --from=chubbyfolio-frontend:latest /home/node/app/dist /app/frontend
RUN mkdir -p /app/public/{media,static}
COPY ./docker_compose/django/collectfrontend.py /app/collectfrontend.py

RUN chown -R django:django /app


EXPOSE 8000

USER django

CMD ["/start.sh"]
