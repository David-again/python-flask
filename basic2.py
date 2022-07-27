from flask import Flask, render_template

app = Flask(__name__)       # Creates tge flask application

@app.route('/')     # This decorator creates the 'home' route
def index(): 
    return render_template("basic2.html")

if __name__ == '__main__':
    app.run(debug=True)
    # app.run()
