from flask import Blueprint, render_template, request
from TheSmack.minilabs.ava_minilab import math
from TheSmack.minilabs.eva_minilab import Foil
from TheSmack.minilabs.linda_minilab import Sum


minilab_bp = Blueprint('minilab Menu', __name__,
                           template_folder='templates',
                           static_folder='static')


@minilab_bp.route('/')
def minilabMenu():
    return "Menu for all of the group's individual mini labs"

@minilab_bp.route('/ava' , methods=['GET', 'POST'])
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

@minilab_bp.route('/risa')
def risa_minilab():
    return "Risa's mini lab page"

@minilab_bp.route('/linda')
def linda_minilab():
    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        sum = Sum(num1, num2)
        print(f"{sum.term1}")
        return render_template("/minilabs/linda-minilab.html", sum=sum)
    return render_template("/minilabs/linda-minilab.html", sum=Sum(0,0))

@minilab_bp.route('/eva' , methods=['GET', 'POST'])
def eva_minilab():
    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        num3 = int(request.form['num3'])
        num4 = int(request.form['num4'])
        foil = Foil(num1, num2, num3, num4)
        print(f"{foil.term1}{foil.term2}{foil.term3}{foil.term4}")
        return render_template("/minilabs/eva-minilab.html", foil=foil)
    return render_template("/minilabs/eva-minilab.html", foil=Foil(0,0,0,0))



