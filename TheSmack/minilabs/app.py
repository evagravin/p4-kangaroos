from flask import Blueprint

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

@ava_minilab_bp.route('/')
def ava_minilab():
    return "Ava's mini lab page"

@risa_minilab_bp.route('/')
def risa_minilab():
    return "Risa's mini lab page"

@linda_minilab_bp.route('/')
def linda_minilab():
    return "Linda's mini lab page"

@eva_minilab_bp.route('/')
def eva_minilab():
    return "Eva's mini lab page"


