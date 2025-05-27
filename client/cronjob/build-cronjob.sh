#!/bin/sh
kubectl delete cronjob agentk-scheduler
docker image rm agent-k/client:v1 -f
docker build -t agent-k/client:v1 -f ./cronjob/Dockerfile ./cronjob