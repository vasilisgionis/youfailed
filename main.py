from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def Login():
    return render_template("templ.html")
  
@app.route('/name')
def hello_name(name):
  return f'Hello {name}!\n'

if __name__ == '__main__':
   app.run(debug=True)
