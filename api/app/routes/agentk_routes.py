import os
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services import yaml_analyzer

router = APIRouter()

@router.post("/analyze")
async def analyze_yaml(file: UploadFile = File(...)):

    valid_mime_types = ["application/x-yaml", "text/yaml"] 
    valid_extensions = [".yaml", ".yml"]

    if (file.content_type not in valid_mime_types):
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a YAML file.")
    
    _, ext = os.path.splitext(file.filename)
    if ext.lower() not in valid_extensions:
        raise HTTPException(status_code=400, detail="Invalid file extension. Only .yaml or .yml allowed.")

    content = await file.read()
    content = content.decode("utf-8")

    result = yaml_analyzer.analyze(content)
    return {
        "status": 200,
        "message": "File analyzed successfully",
        "result": result
    }
