from flask import Blueprint, render_template, request

bubblesort_bp = Blueprint('bubblesort', __name__,
                       template_folder='templates',
                       static_folder='static')

@bubblesort_bp.route('/ava', methods=['GET', 'POST'])
def ava_bubblesort():
    return render_template("/bubbleSort/ava_bubblesort.html")