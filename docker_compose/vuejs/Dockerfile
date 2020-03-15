FROM node:12.16

ARG ENVIRONMENT=production
ARG VUE_APP_ROOT_API
ARG VUE_APP_SITE_URL
ARG VUE_APP_SITE_NAME
ARG VUE_APP_PHONE_NUMBER

WORKDIR /home/node/app

COPY ./frontend/package*.json ./

#RUN npm install -g @vue/cli@4.2.3
RUN npm install

COPY ./frontend .
RUN chown -R node /home/node/app

COPY docker_compose/vuejs/${ENVIRONMENT}/start.sh /start.sh
RUN chmod +x /start.sh \
    && chown node /start.sh

USER node

RUN npm run build

CMD ["/start.sh"]
