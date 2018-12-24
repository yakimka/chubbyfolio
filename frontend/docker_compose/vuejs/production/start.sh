#!/bin/sh
if [ ! -f /home/node/app/dist/index.html ]; then
    npm run build
fi
