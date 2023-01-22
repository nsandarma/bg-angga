from flask import Flask,render_template,request,redirect

app = Flask(__name__)



from app.models import *
from app.routes import *

