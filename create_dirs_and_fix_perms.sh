#!/bin/sh
mkdir -p static
chown 1000:users -R static
mkdir -p media
chown 1000:users -R media
mkdir -p frontend/dist
chown 1000:users -R frontend/dist
