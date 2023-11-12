from app import app
import config
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
# if __name__ == '__main__':
#     app.run(debug=True)

app.config.from_object(config)
# allow track and modify database
db.init_app(app)

@app.route("/database_connection")
def dbTest():
    result = db.engine.execute("SELECT * FROM review")
    return result

if __name__ == '__main__':
    # run server
    server = pywsgi.WSGIServer(('0.0.0.0',5000),app)
    server.serve_forever()