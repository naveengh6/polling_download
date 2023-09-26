import logging

# logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
LOGGER = logging.getLogger('Electoral Logging')
LOGGER.setLevel(logging.INFO)