from flask import Flask, render_template
app = Flask(__name__)

@app.route("/play")
def index():
    return render_template('index_play.html',times=3)

@app.route("/play/<x>")
def multbox(x):
    num=int(x)
    return render_template('index_play.html',times=num)

@app.route("/play/<x>/<color>")
def comult(x,color):
    num=int(x)
    return render_template('index_play.html',times=num,color=color)

if __name__=="__main__":      
    app.run(debug=True)   
