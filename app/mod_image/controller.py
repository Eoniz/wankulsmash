from flask import Blueprint, render_template
from app import db
from app.mod_image.model import Image
import random
import base64

mod_image = Blueprint('image', __name__)


def stringToBase64(s):
    return base64.b64encode(s.encode('utf-8')).decode('ascii')


def base64ToString(b):
    return base64.b64decode(b).decode('utf-8')


def get_random_wankul():
    """
    Util function to get a random wankul
    """
    rand = random.randrange(0, Image.query.count())
    wankul = db.session.query(Image)[rand]

    return wankul


def get_equivalent_wankul(wankul, diff=200):
    """
    Util function to get an equivalent wankul based on other wankul
    AKA : wankul.score - diff < score < wankul.score + diff 
    """
    base_score = wankul.score
    wankuls = Image.query.filter(
        Image.score >= base_score - diff,
        Image.score <= base_score + diff,
        Image.id != wankul.id)

    count = wankuls.count()
    rand = random.randrange(0, count)

    return wankuls[rand]


@mod_image.route('/')
def index():
    wankul_a = get_random_wankul()
    wankul_b = get_equivalent_wankul(wankul_a)

    duel_code = stringToBase64(f'{wankul_a.id}_{wankul_b.id}')
    
    wankuls = [wankul_a, wankul_b]

    return render_template(
        'index.html',
        wankuls=wankuls,
        duel_code=duel_code)
