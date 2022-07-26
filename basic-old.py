from flask import Flask

app = Flask(__name__)

@app.route('/') # home route
def index(): 
    return "<h1>Hello Puppies!</h1>"

@app.route('/information') # a static route
def info(): 
    return "<h1>Puppies are cute</h1>"

@app.route('/puppy/<name>')
def puppy(name):
    # return f"<h1>This is a page for {name}<h1>"
    return "10th letter: {}".format(name[9])

if __name__ == '__main__':
    app.run(debug=True)
    # Important: Do NOT keep debug=True when deploying to production.