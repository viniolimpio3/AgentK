#!/bin/sh
# python -m src.services.db.drop_tables
docker-compose down
docker image rm agent-k/api-agent-k:v1 -f
docker build -t agent-k/api-agent-k:v1 -f .\\Dockerfile .
docker-compose up # -d