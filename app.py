from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "Welcome to Cloud Computing Lab"
@app.route('/student')
def student():
    return "This is the Student page"
if __name__ == '__main__':
    app.run(debug=True)
