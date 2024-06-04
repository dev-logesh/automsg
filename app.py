from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def hello_world():
    return 'Redirect is here https://t.me/cl_me_logesh'

# Run the application
if __name__ == '__main__':
    app.run()