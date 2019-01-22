from flask import Blueprint, render_template, redirect
from app import db
from app.mod_image.model import Image
import random
import base64

mod_image = Blueprint('image', __name__)
_SCORE_DIFF = 200


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
    wankul_b = get_equivalent_wankul(wankul_a, _SCORE_DIFF)

    duel_code = stringToBase64(f'{wankul_a.id}_{wankul_b.id}')
    
    wankuls = [wankul_a, wankul_b]

    return render_template(
        'index.html',
        wankuls=wankuls,
        duel_code=duel_code)


@mod_image.route('/vote/<duel_code>/<wankul_id>')
def vote(duel_code, wankul_id):
    decoded = base64ToString(duel_code)
    wankuls = decoded.split('_')

    wankul_a = Image.query.filter_by(id=wankuls[0]).first()
    wankul_b = Image.query.filter_by(id=wankuls[1]).first()

    winner = wankul_a if wankul_id == wankuls[0] else wankul_b
    looser = wankul_b if winner == wankul_a else wankul_a

    # Si on a bien les deux wankuls
    if wankul_a is not None and wankul_b is not None:
        # Si la différence de score est correcte
        if abs(winner.score - looser.score) <= _SCORE_DIFF:
            diff = winner.score - looser.score
            d = 400 if diff > 400 else diff
            p_d = 1 / (1 + (10 ** (-d / 400)))
            coeff_k_winner = 20 if winner.score <= 2400 else 10 
            coeff_k_looser = 20 if looser.score <= 2400 else 10 

            new_score_winner = round(winner.score + coeff_k_winner * (1 - p_d))
            new_score_looser = round(
                looser.score + coeff_k_looser * (0 - (1 - p_d)))

            winner.score = new_score_winner
            looser.score = new_score_looser

            db.session.commit()
    
    return redirect('/')