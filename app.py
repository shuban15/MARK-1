from curses import termname
from flask import Flask, render_template, request, redirect, url_for

# Create a Flask web application instance.
app = Flask(__name__)

# Define a route for the homepage ('/').
@app.route('/')
def home():
    # When a user visits the root URL, render the index.html file.
    return render_template('index.html')

# Define a route to handle the form submission.
# The methods=['POST'] argument specifies that this route only accepts POST requests.
@app.route('/greet', methods=['POST'])
def greet():
    # Get the data submitted from the form.
    # The 'user_name' key matches the 'name' attribute in the HTML input field.
    user_name = request.form.get('user_name')

    # Simple logic: if the name is provided, return a personalized greeting.
    if user_name:
        return f'Hello, {user_name}!'
    else:
        # If no name is provided, redirect them back to the homepage.
        return redirect(url_for('home'))
@app.route('/print',methods=['GET'])
def print1():
    print(termname)
if __name__ == '__main__':
    # Run the application in debug mode for development.
    app.run(debug=True)