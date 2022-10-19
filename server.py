
from flask import Flask , render_template

app = Flask(__name__) 

@app.route('/play') 
def nivel1():
    return render_template('index.html', num=3, color="blue") 

@app.route('/play/<int:numero>') 
def nivel2(numero):
    return  render_template('index.html', num=numero, color="blue") 

@app.route('/play/<int:numero>/<string:color>' ) 
def nivel3(numero, color):
    return  render_template('index.html', num=numero, color=color) 

if __name__=="__main__": 
    app.run(debug=True)
