from fastapi import APIRouter
from pydantic import BaseModel

from app import logger
from app.services.ping_service import ping, versions

router = APIRouter(prefix="/ping")

class PingData(BaseModel):
    # Define necessary fields
    version: str

@router.post("/")
async def ping_endpoint(data: PingData):
    logger.debug('########## ping endpoint called ##########')
    response = ping(data.dict())
    return response

@router.get("/")
async def version_endpoint():
    logger.debug('########## ping endpoint called ##########')
    response = versions()
    return response