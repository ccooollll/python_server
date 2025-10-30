from app import logger
from app.server import start_server

if __name__ == '__main__':
    logger.info('Starting server')
    start_server()

