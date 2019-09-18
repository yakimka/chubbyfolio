FROM nginx:latest
COPY ./nginx.conf /etc/nginx/nginx.conf
ARG CHUBBYFOLIO_DOMAIN
RUN sed -i "s/example.com/$CHUBBYFOLIO_DOMAIN/g" /etc/nginx/nginx.conf
