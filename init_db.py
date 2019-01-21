from app import db
from app.mod_image.model import Image
from os import listdir
from os.path import isfile, join
import random

path = 'app/static/wankuls/'
images = [f for f in listdir(path) if isfile(join(path, f))]

for image in images:
    # get the name by replacing '_' by whitespace, and removing ext
    name = image.lower().replace('_', ' ').replace('.png', '')
    path = image
    score = random.randrange(1000, 2600)

    existing = Image.query.filter_by(filename=path).first()
    if existing is None:  # only add the image if it's not already in db
        img = Image(name, path, score)
        img.save()

        print(f'{name} is saved on db.')
