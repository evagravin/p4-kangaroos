from flask import Blueprint, render_template, request
from TheSmack.bubblesort.ava_bubblesort import bubble

bubblesort_bp = Blueprint('bubblesort', __name__,
                       template_folder='templates',
                       static_folder='static')

@bubblesort_bp.route('/ava', methods=['GET', 'POST'])
def ava_bubblesort():
    sort = 0
    if request.method == 'POST':
        b = bubble()
        sort = b.bubble_sort()
    return render_template("/bubbleSort/ava_bubblesort.html", sort=sort)

@bubblesort_bp.route('/eva', methods=['GET', 'POST'])
def eva_bubblesort():
    return render_template("/bubbleSort/eva_bubblesort.html")

@bubblesort_bp.route('/risa', methods=['GET', 'POST'])
def risa_bubblesort():
    return render_template("/bubbleSort/risa_bubblesort.html")