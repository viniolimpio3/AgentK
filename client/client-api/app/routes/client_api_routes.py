import os
import json
from fastapi import APIRouter, UploadFile, File, HTTPException, Query

from app.services.db.models import llm_response_history as llm

router = APIRouter()

@router.get("/recomendation")
async def recomendation():
    result = llm.fetch_all()

    return {
        "status": 200,
        "result": [
            {**item, "llm_response": json.loads(item["llm_response"])} for item in result
        ]
    }
