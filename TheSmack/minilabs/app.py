from flask import Blueprint, render_template, request
from TheSmack.minilabs.ava_minilab import math


minilabMenu_bp = Blueprint('minilab Menu', __name__,
                           template_folder='templates',
                           static_folder='static')

ava_minilab_bp = Blueprint('ava-minilab', __name__,
                        template_folder='templates',
                        static_folder='static')

risa_minilab_bp = Blueprint('risa-minilab', __name__,
                           template_folder='templates',
                           static_folder='static')

linda_minilab_bp = Blueprint('linda-minilab', __name__,
                           template_folder='templates',
                           static_folder='static')

eva_minilab_bp = Blueprint('eva-minilab', __name__,
                           template_folder='templates',
                           static_folder='static')

@minilabMenu_bp.route('/')
def minilabMenu():
    return "Menu for all of the group's individual mini labs"

@ava_minilab_bp.route('/' , methods=['GET', 'POST'])
def ava_minilab():
    mean = 0
    median = 0
    mode = 0
    list = ""
    if request.method == 'POST':
        values = request.form['list']
        m = math()
        m.addValues(values)
        mean = m.getAverage()
        median = m.getMedian()
        mode = m.getMode()
        list = m.getList()
    return render_template("/minilabs/ava-minilab.html", mean=mean, median=median, mode=mode, list=list)

@risa_minilab_bp.route('/')
def risa_minilab():
    return "Risa's mini lab page"

@linda_minilab_bp.route('/')
def linda_minilab():
    return render_template("/minilabs/linda-minilab.html")

@eva_minilab_bp.route('/' , methods=['GET', 'POST'])
def eva_minilab():
    return render_template("/minilabs/eva-minilab.html")


