from flask import Flask

i = 0

app = Flask(__name__)

@app.route('/')
def root():
    return "Working"

@app.route('/i/', methods = ['GET', 'POST'])
def iplusplus():
    global i
    i += 1
    return str(i)

if __name__ == "__main__":
    app.run(debug = False,host="0.0.0.0", port=5000)
