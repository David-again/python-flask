
## 1.0 Flask basics
conda create -n myflaskenv flask
- Create a new environment
- Install flask

source activate myflaskenv
- This environment is used for the Flask Basics section (Section 7) of the course.

#### 1.1 Routing
Use decorators to create multiple routes.  Each decorator is of course accompanied by a function, which returns an HTML string, or an HTML template.
In the case of the latter, the HTML template should reside in the folder named `/templates/` at the same level as the python file.

#### 1.2 Choose the correct environment
**Note:** Make sure to change to the correct environment, or the script may not run, resulting in an "authentication error" when trying to access the server at 127.0.0.1:5000
___
*Access to 127.0.0.1 was denied
You don't have authorization to view this page.
HTTP ERROR 403*
___
Change environments with: 
    `source activate myflaskenv`
...assuming that `myflaskenv` is the name of the environment to change to.

## 2.0 Templates
Given that the `/templates/` folder is already created (at the same level as the main python file)
See `basic.py` and `/template/basic.html`
This can be expanded upon by: 
- creating more functions (along with decorators)
- creating more html (template) files
- static files can be referenced from a folder @ same level as templates folder

For an example, see `basic2.py`, `/static/puppy_pic.jpg` and `/template/basic2.html`

#### 2.1 Variables with templates.
You may "inject" Python code, such as variables, into html, similar to what JSX does for JavaScript/ReactJS.


#### 2.2 Template Control Flow
Use the Flask Snippets extension in VS Code:
- `fif:    Flask if`
- `ffor:   Flask for`
- `felif:  Flask if-elif-else`

Just begin by typing 'f' and sort through the options.

#### 2.3 Template Inheritance
Multiple pages re-use the same template, because of parts that they have in common, such as navbar, footer, etc...
Scenario: `02-base.py` is the script; `02-base.html` is the base template; `02-home.html` and `02-puppy.html` are 2 other pages that 'extend' the base file

The base file (e.g. base.html) contains the flask block: 
-    `{% block content %}`
-    `{% endblock %}`
<!-- Use fblock for the above. -->

The home.html file contains the `extends` line, as well as the block syntax and the unique code.
- `{% extends "base.html" %}`
- `{% block content %}`
- `{% endblock %}`

