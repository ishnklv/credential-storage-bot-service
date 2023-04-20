#!/bin/sh

MONGODB_HOST="localhost"
MONGODB_PORT="27017"

if nc -w 1 -z $MONGODB_HOST $MONGODB_PORT; then
  echo "MongoDB is active"
  python3 main.py
else
  echo "MongoDB is not active"
  exit 1
fi