#!/bin/sh
if [ ! -f /home/node/app/dist/index.html ]; then
    npm run build
    find ./dist -type f -name '*.map' -delete
fi
