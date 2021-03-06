from flask import Blueprint, render_template, request
from TheSmack.bubblesort.ava_bubblesort import bubble
from TheSmack.bubblesort.eva_bubblesort import bubble_sort, bubble_sort2
from TheSmack.bubblesort.risa_bubblesort import bubblesort
from TheSmack.bubblesort.linda_bubblesort import linda


bubblesort_bp = Blueprint('bubblesort', __name__,
                       template_folder='templates',
                       static_folder='static')

@bubblesort_bp.route('/ava', methods=['GET', 'POST'])
def ava_bubblesort():
    #set default values for variables list and sort
    list = 0
    sort = 0
    if request.method == 'POST':
        #get values from form
        values = request.form['list']
        b = bubble()
        #call addValues function from bubblesort.py
        b.addValues(values)
        #getList
        list = b.getList()
        #sort the lists
        sort = b.sort()
    return render_template("/bubbleSort/ava_bubblesort.html", list=list, sort=sort)

@bubblesort_bp.route('/eva', methods=['GET', 'POST'])
def eva_bubblesort():
    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        num3 = int(request.form['num3'])
        num4 = int(request.form['num4'])
        first_list = [num1, num2, num3, num4]
        unsorted_list = [num1, num2, num3, num4]
        sorted_list = bubble_sort(unsorted_list)
        return render_template("/bubbleSort/eva_bubblesort.html", num1=num1, num2=num2, num3=num3, num4=num4, unsorted_list=unsorted_list, sorted_list=sorted_list, first_list=first_list)
    return render_template("/bubbleSort/eva_bubblesort.html")

@bubblesort_bp.route('/evaform2', methods=['GET', 'POST'])
def eva_bubblesort2():
    if request.method == 'POST':
        string1 = request.form['string1']
        string2 = request.form['string2']
        string3 = request.form['string3']
        string4 = request.form['string4']
        list2 = [string1, string2, string3, string4]
        list = [string1, string2, string3, string4]
        sorted_list2 = bubble_sort2(list)
        return render_template("/bubbleSort/eva_bubblesort.html", string1=string1, string2=string2, string3=string3, string4=string4, list2=list2, list=list, sorted_list2=sorted_list2)
    return render_template("/bubbleSort/eva_bubblesort.html")

@bubblesort_bp.route('/risa', methods=['GET', 'POST'])
def risa_bubblesort():
    if request.method == 'POST':
        calc1 = int(request.form['calc1'])
        calc2 = int(request.form['calc2'])
        calc3 = int(request.form['calc3'])
        calc4 = int(request.form['calc4'])
        calc5 = int(request.form['calc5'])
        calc6 = int(request.form['calc6'])
        calc7 = int(request.form['calc7'])
        calc8 = int(request.form['calc8'])
        calc9 = int(request.form['calc9'])
        calc10 = int(request.form['calc10'])
        mycalclist = [calc1, calc2, calc3, calc4, calc5, calc6, calc7, calc8, calc9, calc10]
        mynumlist = [calc1, calc2, calc3, calc4, calc5, calc6, calc7, calc8, calc9, calc10]
        list_sorted = bubblesort(mycalclist)
        return render_template("/bubbleSort/risa_bubblesort.html", calc1=calc1, calc2=calc2, calc3=calc3, calc4=calc4, calc5=calc5, calc6=calc6, calc7=calc7, calc8=calc8, calc9=calc9, calc10=calc10, mynumlist=mynumlist, list_sorted=list_sorted, mycalclist=mycalclist)
    return render_template("/bubbleSort/risa_bubblesort.html")


#a decorator that prompts a specific page of the website
@bubblesort_bp.route('/linda', methods=['GET', 'POST'])
#define route function
def linda_bubblesort():
    #initialize the variables unsort and sort to 0
    unsort = 0
    sort = 0
    #use POST method to add/update data
    if request.method == 'POST':
        #request values from form
        values = request.form['list']
        l = linda()
        l.addValues(values)
        #pass the values into the list
        sort = l.sort()
        unsort = request.form['list']
    return render_template("/bubblesort/linda_bubblesort.html", sort=sort, unsort=unsort)

