from flask import Blueprint, render_template, session
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

@groups_bp.route('/delnorte/posts')
def delnorte_posts():
    return render_template("/groups/delNorte_posts.html")


@groups_bp.route('/mtCarmel')
def mtCarmel_groups():
    users=get_users("Mountt Carmel Hight School")
    return render_template("/groups/mtCarmel.html", users=users)

@groups_bp.route('/ranchobernardo')
def ranchobernard_groups():
    users=get_users("Rancho Bernardo High School")
    return render_template("/groups/ranchoBernardo.html", users=users)

@groups_bp.route('/poway')
def poway_groups():
    users=get_users("Poway High School")
    return render_template("/groups/poway.html", users=users)

@groups_bp.route('/westview')
def westview_groups():
    users=get_users("Westview High School")
    return render_template("/groups/westview.html", users=users)
