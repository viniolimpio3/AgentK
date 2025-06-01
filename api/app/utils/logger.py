import logging

logging.basicConfig(
    level = logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='/app/logs/api-agentk.log', 
    filemode='a'
)

logger = logging.getLogger(__name__)