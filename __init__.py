from flask import Flask
import os

app = Flask(__name__)
# Port number is required to fetch from env variable
# http://docs.cloudfoundry.org/devguide/deploy-apps/environment-variable.html#PORT
app.config.from_mapping(
	SECRET_KEY='dev',
	DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
)

cf_port = os.getenv("PORT")

# ensure the instance folder exists
try:
	os.makedirs(app.instance_path)
except OSError:
	pass

# Only get method by default
@app.route('/hello')
def hello():
    return 'Hello World'

from . import db
db.init_app(app)

if __name__ == '__main__':
	if cf_port is None:
		app.run(host='0.0.0.0', port=5000, debug=True)
	else:
		app.run(host='0.0.0.0', port=int(cf_port), debug=True)
