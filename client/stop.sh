#!/bin/sh
# STOP Client API
kubectl delete svc client-api-k
kubectl delete deployment client-api-k

# Build CronJob
kubectl delete cronjob agentk-scheduler