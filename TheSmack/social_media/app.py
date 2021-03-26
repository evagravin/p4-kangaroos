from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, app
from flask_sqlalchemy import SQLAlchemy



trending_bp = Blueprint('trending', __name__,
                        template_folder='templates',
                        static_folder='static')

createSmack_bp = Blueprint('createSmack', __name__,
                        template_folder='templates',
                        static_folder='static')

smackDM_bp = Blueprint('smackDM', __name__,
                           template_folder='templates',
                           static_folder='static')


@trending_bp.route('/')
def trending():
    return "Trending Page"


@createSmack_bp.route('/')
def createSmack():
    return "Create a Smack page"

@smackDM_bp.route('/')
def smackDM():
    return "Smack(DM) someone"



