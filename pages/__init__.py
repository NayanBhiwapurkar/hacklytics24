import os
import toml
import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)


with open('../.streamlit/secrets.toml', 'r') as file:
    data = toml.load(file)
    for key_name in ["OPENAI_API_KEY", "TRAVERSAAL_API_KEY"]:
        os.environ[key_name] = data[key_name]
        logger.info(f"{key_name}={data[key_name]}")
