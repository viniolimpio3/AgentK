#!/bin/sh
python -m src.services.db.drop_tables
kubectl delete cronjob agentk-scheduler
docker image rm agent-k/client:v1 -f
docker build -t agent-k/client:v1 -f .\\Dockerfile .
kubectl apply -f .\\agentk-cronjob.yaml