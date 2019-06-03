from flask import Flask
import json

i = 0

app = Flask(__name__)

@app.route('/')
def root():
    return "Working"

@app.route('/param')
def get_param():
    return request.args.get('param')

@app.route('/i/', methods = ['GET', 'POST'])
def iplusplus():
    global i
    i += 1
    return json.dumps({'i': str(i)}, sort_keys=True, indent=4, separators=(',', ': '))

if __name__ == "__main__":
    app.run(debug = False,host="0.0.0.0", port=5000)
