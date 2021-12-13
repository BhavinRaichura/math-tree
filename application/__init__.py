import flask
from flask import Flask 

app=Flask(__name__)

from application import routes
from application import newton_rapson1 as nr 
from application import bisection as bs
from application import falsePositionMethod as fpm
