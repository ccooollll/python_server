import os
import logging
import sys
import munch
import yaml
import yamale
from yamale.yamale_error import YamaleError
from importlib.resources import files

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('flowops')

app_config = None
"""
A package-wide configuration object.
This is a dictionary that provides attribute-style access.
"""

# Ensure APP_CONFIG environment variable is set
if 'APP_CONFIG' not in os.environ:
    raise SystemExit('Please set APP_CONFIG')

# Fetch configuration filename from the environment variable
config_filename = os.environ['APP_CONFIG']

# Check if the configuration file exists
if not os.path.exists(config_filename):
    logger.fatal(f'Configuration file: {config_filename} does not exist.')
    sys.exit(1)

# Validate the configuration against the predefined schema
schema_filename = str(files('app.config') / 'schema.yaml')
config_schema = yamale.make_schema(schema_filename)
config_data = yamale.make_data(config_filename)
try:
    yamale.validate(config_schema, config_data, strict=True)
except YamaleError as e:
    # Log errors if the validation fails
    res = e.results[0]
    logger.error(f'Error encountered while loading configuration file: {res.data}')
    for error_msg in res.errors:
        logger.error(error_msg)
    sys.exit(2)

# Load and munchify the configuration data
with open(config_filename) as f:
    app_config = munch.munchify(yaml.safe_load(f))
    logger.debug(f'Loaded config file: {config_filename}')
