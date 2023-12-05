from app import app
import config
from exts import db


# if __name__ == '__main__':
#     app.run(debug=True)

if __name__ == '__main__':
    # run server
    server = pywsgi.WSGIServer(('0.0.0.0',5000),app)
    server.serve_forever()