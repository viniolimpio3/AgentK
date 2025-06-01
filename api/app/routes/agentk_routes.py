import os
from fastapi import APIRouter, UploadFile, File, HTTPException, Query
from app.services import yaml_analyzer
from app.utils.logger import logger

router = APIRouter()

@router.post("/analyze")
async def analyze_yaml(
    file: UploadFile = File(...),
    model: str = Query(None)
):

    try:
        logger.info(f"Received file: {file.filename} with content type: {file.content_type}")
        valid_mime_types = ["application/x-yaml", "text/yaml"] 
        valid_extensions = [".yaml", ".yml"]

        if (file.content_type not in valid_mime_types):
            raise HTTPException(status_code=400, detail="Invalid file type. Please upload a YAML file.")
        
        _, ext = os.path.splitext(file.filename)
        if ext.lower() not in valid_extensions:
            raise HTTPException(status_code=400, detail="Invalid file extension. Only .yaml or .yml allowed.")

        content = await file.read()
        content = content.decode("utf-8")
        logger.info(f"File content length: {len(content)} characters")
        result = yaml_analyzer.analyze(content, model)  # use model se desejar

        if "error" in result:
            return {
                "status": 500,
                "message": "An error occurred while analyzing the YAML content.",
                "error": result["error"]
            }

        return {
            "status": 200,
            "message": "File analyzed successfully",
            "result": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while processing the file: {str(e)}")
