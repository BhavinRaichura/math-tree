from math import *

def falsep(xn,ro,a,b):
    sen =f'<h3><br>Given function is f(x) = {xn}<br>proints are a = {a} and b = {b}</h3>'
    xn=xn.replace("^",'**')
    def f(x):
        try:
            eq=round(eval(xn),ro+1)
        except:
            return sen + '<br><h3>invalid function</h3>'
        return eq
   
    if a<b and (f(a)*f(b))<0:
        i=0
        c=0
        while True:
            if i==41:
                return "<h3>condition infinity loop</h3><h3>it will be taking more than 40 iteration</h3>" + sen
            a=round(a,ro+2)
            b=round(b,ro+2)
            fsub=round((f(b)-f(a)),ro+2)
            sub=round((b-a),ro+2)
            i=i+1
            sen=sen+f"<br><br><h3>------Iteration {i}------</h3>"
            c=round(a-f(a)*((b-a)/(f(b)-f(a))),ro+2)
            sen=sen+f'<br>c = a - f(a) * ( (b-a) / (f(b)-f(a)) )<br>c = {a} - ({f(a)}) * ( {sub} / {fsub} ) <br>c = {c}<br>f(c)=f({c})={f(c)}'
            
            if round(f(c),ro)==0.0:
                break
            if f(c)*f(a)<0:
                sen=sen+f'<br>Here f({c}) = {f(c)} > 0<br>So, Root lies between a = {a} and b = {c} '
                b=c
            elif f(c)*f(b)<0:
                sen=sen+f'<br>Here f({c}) = {f(c)} < 0<br>So, Root lies between a = {c} and b = {b} '
                a=c
        return  sen + f'<br><h3>Approximate root using False Position mehtod is {c}</h3>'