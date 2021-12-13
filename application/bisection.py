from math import *

def bisec(xn,ro,a,b):
    def  func(xn,x,ro):
        try:
            xn=xn.replace("^",'**')
            calfn= eval(xn)
        except:
            return "invalid"
        calfn= round(calfn,ro)
        return calfn
    sen = f"<h3>Given Function f(x)={xn}</h3><br><h3>find root between a={a} and b={b}."
    if func(xn,a,ro)== "invalid":
        sen=sen + '<br><h3>invalid function</h3>'
        return sen
    if (func(xn,a,ro)*func(xn,b,ro))>=0:
        sen='<h3>wrong "a" and "b"</h3>'
        return sen
    else:
        c=a
        i=0
        while (b-a)>=(1/10**ro):
            i=i+1
            c=round((a+b)/2,ro)
            if i==25:
                return f'<br><h3>Infinity loop</h3><br>it will take more than {i} iteration <br>' +sen
            
            sen = sen+f'<br><br><h3>------Iteration {i}------</h3><br>f(a) = {func(xn,a,ro)} and <br>f(b)= {func(xn,b,ro)}<br>t = (a+b)/2 = {c}<br>f(t) = {func(xn,c,ro)}'
            
            if func(xn,c,ro)==0.0:
                break

            if func(xn,c,ro)*func(xn,a,ro)<0:
                b=c
                sen = sen + f'<br>because f(a)*f(t)<0 so the root is lie between a and t.<br>b = t<br>[a,b] =[{a},{b}]'
            else:
                a=c
                sen = sen + f'<br>because f(b)*f(t)<0 so the root is lie between t and b<br>a = t<br>[a,b] =[{a},{b}]'
        sen = sen + f'<br><h3>approximate root is {c}</h3>'
        return sen
