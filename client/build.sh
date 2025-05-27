#!/bin/sh
# Build Client API
kubectl delete svc client-api-k
kubectl delete deployment client-api-k
docker image rm agent-k/client-api-k:v1 -f
docker build -t agent-k/client-api-k:v1 -f ./client-api/Dockerfile ./client-api

# Build CronJob
kubectl delete cronjob agentk-scheduler
docker image rm agent-k/client:v1 -f
docker build -t agent-k/client:v1 -f ./cronjob/Dockerfile ./cronjob

# Apply client-api & CronJob
kubectl apply -f ./client-agentk.yaml