from flask import Flask, render_template

app = Flask(__name__)       # Creates the flask application

@app.route('/')     # This decorator creates the 'home' route
def index(): 
    return render_template("02-home.html")

@app.route('/puppy/<name>')
def puppy(name):
    return render_template("02-puppy.html", name=name)

if __name__ == '__main__':
    app.run(debug=True)
    # app.run()
