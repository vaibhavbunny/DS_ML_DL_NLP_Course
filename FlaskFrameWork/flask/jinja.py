## Building url dynamically,
## Variable Rule
## Jinja 2 Template Engine

## Jinja 2 Template Engine
'''
{{ }} expressions to print output in html
{%...%} conditions , for loops, while loops
{#...#} this is for comments
'''

from flask import Flask,render_template,request,redirect,url_for

## render_template ---> redirtectiong to a particular file it helps in doing that. specifically html file rendering.f

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome to this Course</h2></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

# @app.route("/submit",methods=['GET','POST'])
# def submit():
#     if request.method=='POST':
#         name = request.form['name']
#         return f"Hello {name}"
#     return render_template('form.html')
## Variable Rule -- > restricting the parameter accordingly. below score is specified to integer.
@app.route("/success/<int:score>") ## the score parameter is passable in the below function.
def success(score):
    res=""
    if score>=50:
        res = "PASSED"
    else:
        res = "FAILED"
    return render_template('result.html',result=res)

## Variable Rule -- > restricting the parameter accordingly. below score is specified to integer.
@app.route("/successres/<int:score>") ## the score parameter is passable in the below function.
def successres(score):
    res=""
    if score>=50:
        res = "PASSED"
    else:
        res = "FAILED"
    exp = {'score':score , 'res':res}
    return render_template('result1.html',result=exp)

@app.route("/successif/<int:score>") ## the score parameter is passable in the below function.
def successif(score):
    return render_template('result.html',result=score)

@app.route("/fail/<int:score>")
def fail(score):
    return render_template('result.html',result=score)

@app.route("/submit",methods=['GET','POST'])
def submit():
    total_score = 0
    if request.method=='POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        datascience = float(request.form['datascience'])
        total_score = (science+maths+c+datascience)/4
        return redirect(url_for('successres',score=total_score))
    else:
        return render_template('getresult.html')


    


if __name__ == "__main__":
    app.run(debug=True)