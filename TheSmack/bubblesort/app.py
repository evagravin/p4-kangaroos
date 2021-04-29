from flask import Blueprint, render_template, request
from TheSmack.bubblesort.ava_bubblesort import bubble
from TheSmack.bubblesort.eva_bubblesort import bubble_sort, bubble_sort2

bubblesort_bp = Blueprint('bubblesort', __name__,
                       template_folder='templates',
                       static_folder='static')

@bubblesort_bp.route('/ava', methods=['GET', 'POST'])
def ava_bubblesort():
    list = 0
    sort = 0
    if request.method == 'POST':
        values = request.form['list']
        b = bubble()
        b.addValues(values)
        list = b.getList()
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
    return render_template("/bubbleSort/risa_bubblesort.html")