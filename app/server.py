import uvicorn
from fastapi import FastAPI
from app import logger
from app.api import api_router
from app.config.engine import app_config

# Load server configuration from app_config
host = app_config.server.HOST
port = app_config.server.PORT
route = app_config.server.ROUTE
LOG_LEVEL = app_config.LOG_LEVEL

# Initialize the FastAPI application
app = FastAPI()

# Include the API router
app.include_router(api_router, prefix=route)

# Lifecycle events for startup and shutdown
@app.on_event("startup")
async def startup_event():
    logger.info("########## Starting App Event ##########")
    # You can add startup actions here (e.g., test DB connection if necessary)
    try:
        # async with engine.begin() as conn:
        #     await conn.execute(text("SELECT 1"))
        logger.info("Startup successfully.")
    except Exception as e:
        logger.error(f"Failed to connect to the database: {e}")
        raise e

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("########## Shutting Down App Event ##########")
    # Dispose the database engine
    # await engine.dispose()

# Function to start the server
def start_server():
    logger.info("########## Starting App Server ##########")
    logger.info(f"Server running at http://{host}:{port}{route}")
    uvicorn.run(app, host=host, port=port, log_level='warning')
