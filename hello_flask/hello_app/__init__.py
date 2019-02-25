from flask import Flask
import logging
app = Flask(__name__)
# To run type this "python3 -m flask run" on terminal
app.config.from_object('hello_app.config_cosmos')
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import hello_app.views