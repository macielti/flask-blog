from flask import Flask
#import configuration data
from config import Configuration

app = Flask(__name__)
#use values from our configuration object
app.config.from_object(Configuration)
