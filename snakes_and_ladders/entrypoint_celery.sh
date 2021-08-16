#!/bin/sh
celery multi start w1 w2 w3 -A kamikaze3 --pidfile=$PWD/logs/%n.pid --logfile=$PWD/logs/%n%I.log --loglevel=INFO --concurrency=1
#celery multi start w1 w2 w3 -A kamikaze3 --pidfile=logs/%n.pid --logfile=logs/%n%I.log --loglevel=INFO --concurrency=1
tail -f /dev/null
