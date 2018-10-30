import os
from app import create_app


config_name = "development"
app = create_app(config_name)
# method to run the flask app
if __name__ == '__main__':
    app.run()