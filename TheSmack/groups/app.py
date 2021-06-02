from flask import Blueprint, render_template
from TheSmack.users.user import get_users


groups_bp = Blueprint('groups', __name__,
                          template_folder='templates',
                          static_folder='static')

@groups_bp.route('/')
def groups():
    return render_template("/groups/groups.html")


@groups_bp.route('/delnorte')
def delnorte_groups():
    users=get_users("Del Norte High School")
    return render_template("/groups/delNorte.html", users=users)


@groups_bp.route('/mtCarmel', methods=['GET' 'POST'])
def mtCarmel_groups():
    return render_template("/groups/mtCarmel.html")
