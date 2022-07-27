from flask import Flask, render_template

app = Flask(__name__)       # Creates tge flask application

@app.route('/')     # This decorator creates the 'home' route
def index(): 
    my_list = list("12345")
    dogs = ["Suzie", "Zoey", "Timmy"]
    return render_template("basic_flow.html", 
                my_list = my_list, dogs = dogs)

if __name__ == '__main__':
    app.run(debug=True)
    # app.run()
