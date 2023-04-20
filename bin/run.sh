#!/bin/sh

if [ -f .env ]; then
  source .env
fi

if nc -w 1 -z $MONGODB_HOST $MONGODB_PORT; then
  echo "MongoDB is active"
  python3 main.py
else
  echo "MongoDB is not active"
  exit 1
fi