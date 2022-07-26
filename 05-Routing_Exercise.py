# Set up your imports here!
# import ...
from flask import Flask 
# from flask import request     #I'm not sure what this line does... Didn't need it to run the code.

app = Flask(__name__)

@app.route('/') # Fill this in!
def index():
    # Welcome Page
    # Create a generic welcome page.
    # return "<h1>This is the home page</h1>"
    return '''<h1>Welcome to the home page!</h1> 
    <h3> Go to <em> /puppy_latin/&ltname&gt </em> to see your name in latin!!! </h3>
    '''

@app.route('/puppy_latin/<name>') # Fill this in!
def puppylatin(name):
    # This function will take in the name passed
    # and then use "puppy-latin" to convert it!

    # HINT: Use indexing and concatenation of strings
    # For Example: "hello"+" world" --> "hello world"
    lastChar = name[-1].lower()
    newString = f"<h1>Puppy-latin for {name} is {name[:-1]}"
    if lastChar == "y":
        newString += "iful"
    else: 
        newString += lastChar + "y"
    return newString
    
if __name__ == '__main__':
    # Fill me in!
    app.run(debug=True)
