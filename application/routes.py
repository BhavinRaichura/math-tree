from application import app
import flask
from flask import Flask, redirect, url_for,render_template,request, Markup 
import random

from application import newton_rapson1 as nr 
from application import bisection as bs
from application import falsePositionMethod as fpm


from flask_wtf import FlaskForm
from wtforms import Form,StringField, IntegerField
from wtforms.validators import DataRequired



app.config["SECRET_KEY"] = '571ebf8e13ca209536c29be68d435c00'

class MyForm(Form):
    name = StringField('name', validators=[DataRequired()])
    fx = StringField('f(x)', validators=[DataRequired()])
    deci = IntegerField('Decimal places', validators=[DataRequired()])
    a= IntegerField('a',validators=[DataRequired()])
    b= IntegerField('b',validators=[DataRequired()])




@app.route('/')
def home():
    title ="Math Tree"
    return render_template('base.html',title=title)


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    form = MyForm(request.form)
    if form.validate_on_submit():
        myname =form.name.data
        print(myname)
        return redirect('/success')
    return render_template('submit.html', form=form)
            

@app.route('/newtonRaphson', methods=['POST','GET'])
def newtonRaphson():
    global sol
    title='Newton Raphson Method'
    if request.method == 'POST':
        Nfx=request.form['fx']
        Ndfx=request.form['dfx']
        Ndeci =request.form['deci']
        Nxo=request.form['xo']
        #if Nxo is empty
        if Nxo=="":
            Nxo = random.randint(1,3)
        
        #this return is for onother page
        #return redirect(url_for('home',f=Nfx,df=Ndfx,xo=Nxo,do=Ndeci))
        #return redirect(url_for('index'))
        sol=nr.mynewtonRaphson(Nfx.lower(),Ndfx.lower(),int(Ndeci),float(Nxo))
        sol= sol.replace("\n",'<br>')
        sol=Markup(sol)
        return render_template('base.html',title=title,solu=sol)
        #used for same page solution 
    return render_template('base.html',title=title)


@app.route('/bisectionMethod', methods=['POST','GET'])
def bisectionMethod():
    global sol
    bmform = MyForm(request.form)
    title="Bisection Method"
    if request.method == 'POST':
        Nfx = bmform.fx.data
        Ndeci = bmform.deci.data
        Nx0= bmform.a.data
        Nx1= bmform.b.data
        #Nfx=request.form['fx']
        #Ndeci =request.form['deci']
        #Nx0=request.form['x1']
        #Nx1=request.form['x2']
        sol=bs.bisec(Nfx.lower(),int(Ndeci),float(Nx0),float(Nx1))
        sol=Markup(sol)
        return render_template('base.html',solu=sol,title=title, form=bmform)
        #used for same page solution 
    return render_template('base.html',title=title,form=bmform)

@app.route('/FalsePositionMethod', methods=['POST','GET'])
def FalsePositionMethod():
    global sol
    title="False Position Method"
    if request.method == 'POST':
        Nfx=request.form['fx']
        Ndeci =request.form['deci']
        Nx0=request.form['a']
        Nx1=request.form['b']
        sol=fpm.falsep(Nfx.lower(),int(Ndeci),float(Nx0),float(Nx1))
        sol=Markup(sol)
        print("False Position Method printed")
        return render_template('base.html',solu=sol,title=title)
        #used for same page solution 
    return render_template('base.html',title=title)

 