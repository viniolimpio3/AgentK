from fastapi import FastAPI
from app.routes import client_api_routes 

app = FastAPI()

app.include_router(client_api_routes.router, prefix="/api", tags=["Agentk"])
