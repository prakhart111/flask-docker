from flask import Flask

# python -m flask run 
# to run the server

app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
    return 'GET Request'

# post request
@app.route('/post', methods=['POST'])
def test():
    return 'This is a POST request'