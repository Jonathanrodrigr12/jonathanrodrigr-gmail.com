import os
import unittest
import json

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from Project.Api._init_ import create_app, db
from Project._init_ import blueprint
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint

HOST_SWAGGER = os.getenv('HOST_SWAGGER', 'localhost:5000')
SWAGGER_URL = '/swagger'
API_URL = 'Project/Api/static/swagger.json'
PATH_JSON = 'Project'+API_URL
app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
with open(API_URL, 'r+') as filejson:
        data = json.load(filejson)
        data['host'] = HOST_SWAGGER # <--- add `id` value.
        filejson.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, filejson, indent=4)
        filejson.truncate()     # remove remaining part
    ### swagger specific ###
swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        '/static/swagger.json',
        config={
            'app_name': "Seans-Python-Flask-REST-Boilerplate"
        }
    )

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

app.register_blueprint(blueprint)

cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)
app.run()
@manager.command
def run():
    app.run()

@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

# if __name__ == '__main__':
#     manager.run()