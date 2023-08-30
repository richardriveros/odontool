from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def hello():
    ''' return ("<h1>Hola Richard</h1>") '''
    return render_template('home.html')

print(__name__)

if __name__ == "__main__":
   '''print("Estoy dentro del If")'''
   app.run('0.0.0.0', debug=True)