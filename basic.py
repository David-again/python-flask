from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')     # The 'home' route
def index(): 
    return render_template("basic.html")

if __name__ == '__main__':
    app.run(debug=True)
    # app.run()
