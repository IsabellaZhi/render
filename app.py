from flask import *
from whitenoise import WhiteNoise

app = Flask(__name__)
app.wsgi_app = WhiteNoise(app.wsgi_app, root='static/', prefix='static/', index_file='index.htm', autorefresh=True)
    # wsgi means linking a sub module to the server
    # prefix is where the files live

@app.route('/', methods=['GET'])
    # The string is what I want the web addredd to be
def hello():
    return make_response("Hello, this is my test site!")


if __name__ == '__main__':
    # render running this file will not have name = main
    app.run(threaded=True, port = 5000)