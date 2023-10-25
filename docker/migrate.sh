#!/bin/bash

./manage.py collectstatic --no-input
./manage.py migrate --no-input

exec "$@"
