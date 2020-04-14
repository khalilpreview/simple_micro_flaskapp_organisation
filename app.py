from flask import Flask , render_template , redirect , url_for , request 

# Flask app initialisation
app = Flask(__name__)

# app configuration from config.py
app.config.from_pyfile('config.py')



@app.route('/')
def home():
    return 'Welcome Home from app.py'



if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
