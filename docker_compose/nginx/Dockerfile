FROM nginx:1.16

COPY ./docker_compose/wait-for-it.sh /bin/wait-for-it
RUN chmod +x /bin/wait-for-it
COPY ./docker_compose/nginx/nginx.conf /etc/nginx/nginx.conf
ARG CHUBBYFOLIO_DOMAIN
RUN sed -i "s/example.com/$CHUBBYFOLIO_DOMAIN/g" /etc/nginx/nginx.conf
