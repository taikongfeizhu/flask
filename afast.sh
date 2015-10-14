#!/usr/bin/env bash
if [ $# -eq 1 ];then
    echo "tasking $1:"
    python manage.py runserver -h 0.0.0.0 -p $1 -r
else
    python manage.py runserver -h 0.0.0.0 -p 8888 -r
fi
