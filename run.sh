#!/usr/bin/env bash
if [ $# -eq 1 ];then
    echo "tasking $1:"
    python index.py runserver -h 0.0.0.0 -p $1 -r
else
    python index.py runserver -h 0.0.0.0 -p 8888 -r
fi
