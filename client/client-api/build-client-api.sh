#!/bin/sh
kubectl delete svc client-api-k
kubectl delete deployment client-api-k
docker image rm agent-k/client-api-k:v1 -f
docker build -t agent-k/client-api-k:v1 -f ./client-api/Dockerfile ./client-api