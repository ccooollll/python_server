import os
import logging
from app.config.engine import app_config
log_level = app_config.LOG_LEVEL
log_level = logging.getLevelNamesMapping().get(log_level, 10)

logger = logging.getLogger('App')
logger.setLevel(log_level)
ch = logging.StreamHandler()
ch.setLevel(log_level)
ch.setFormatter(logging.Formatter('%(asctime)-15s [%(module)s] %(levelname)s | %(message)s'))
logger.addHandler(ch)