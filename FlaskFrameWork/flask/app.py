from flask import Flask

'''
It creates an instance of the Flask Class
which will be ur WSGI 
'''

##WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this Flask Course. This should be an amazing course."

@app.route("/index")
def index():
    return "Welcome to this index page"


if __name__ == "__main__":
    app.run(debug=True)


