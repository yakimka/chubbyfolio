FROM node:11.4.0

WORKDIR /home/node/app

COPY package*.json ./

RUN npm install
COPY . .
RUN chown -R node /home/node/app

COPY ./docker_compose/vuejs/production/start.sh /start.sh
RUN chmod +x /start.sh \
    && chown node /start.sh

USER node

CMD ["/start.sh"]
