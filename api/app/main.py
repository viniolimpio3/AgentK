from fastapi import FastAPI
from app.routes import agentk_routes 

app = FastAPI()

app.include_router(agentk_routes.router, prefix="/api", tags=["Agentk"])
