
import random
from math import *
# Function to find the root
# "nDecimal" is place of decimal point
# "e1" is function 
# "e2" is derivative of function 
def mynewtonRaphson(e1,e2,nDecimal, x):
    i=1
    sen=f"\n\nf(x) = {e1}\nf'(x) = {e2}\nx</sub>0</sub> = {x},\t\tDecimal place = {nDecimal}\n\n"
    sen= sen + "\n\n"+ f"<h3>------Iteration {i}------</h3>"
    # to calculate e1 and e2 we use in-buid-function eval
    try:
        exp1=round(eval(e1.replace("^","**")),nDecimal)
        exp2=round(eval(e2.replace("^","**")),nDecimal)
    except:
        sen =sen + "\nInvalid Function\nYou can define function either x^3+3*x^2+5*x+1 or x*x*x+3*x*x+5*x+1"
        return sen
    
    if exp2 ==0:
        return sen + f"undefine condition for Derivative is zero (f'(x<sub>{i-1}</sub>) = 0). So method terminated."

    sen= sen + "\n"+ f"f(x<sub>0</sub>) = {exp1}\nf'(x<sub>0</sub>) = {exp2}"
    
    
    # calculation of root
    x0= x
    sen = sen + "\n" + f"x<sub>{i}</sub>= x<sub>{i-1}</sub> - f(x<sub>{i-1}</sub>)/f'(x<sub>{i-1}</sub>)\nx<sub>{i}</sub> = {x0} - ({exp1}/{exp2})"
    h=round(exp1/exp2,nDecimal)
    x1=round(x0-h,nDecimal)
    i=1
    sen= sen + "\n"+ f'<b>x<sub>1</sub> = {x1}</b>'
    
    while x1!=x0:
        i=i+1
        if i==41:
            return "<h3>condition infinity loop</h3><h3>it will be taking more than 40 iteration</h3>" + sen
        x=x1
        sen= sen + "\n\n"+ f"<h3>------Iteration {i}------</h3>"
        exp1=round(eval(e1.replace("^","**")),nDecimal)
        exp2=round(eval(e2.replace("^","**")),nDecimal)
        if exp2 ==0:
            return sen + f"undefine condition for Derivative is zero (f'(x<sub>{i-1}</sub>) = 0). So method terminated."

        sen= sen + f"\nf(x<sub>{i-1}</sub>) = {exp1}\nf'(x<sub>{i-1}</sub>) = {exp2} "
        
        # calculation of root
        h=round(exp1/exp2,nDecimal)
        x1=round(x-h,nDecimal)
        sen = sen + "\n" + f"x<sub>{i}</sub> = x<sub>{i-1}</sub> - f(x<sub>{i-1}</sub>)/f'(x<sub>{i-1}</sub>)\nx<sub>{i}</sub> = {x1} - ({exp1}/{exp2})"
        sen= sen + f'\n<b>x<sub>{i}</sub> = {x1}</b>'
        
        if x1==x:
            sen= sen 
            break
            # if n^th and n-1^th both values of root are equal for "nDecimal"
            # then while loop will be breaked
	    
    sen = sen +"\n"+ f"\n<h3>Answer : Approximate root of the equation {e1} = {x}</h3>"
    return sen 
 


 # Initial values assumed

 