from app import db


class Image(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified_at = db.Column(
        db.DateTime,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())
        
    name = db.Column(db.String(50), nullable=False)
    filename = db.Column(db.String(50), nullable=False)
    score = db.Column(db.Float, nullable=False)

    def __init__(self, name, filename, score):
        self.name = name
        self.filename = filename
        self.score = score

    def __repr__(self):
        return f"[Image {self.name} / {self.filename} / {self.score}]"

    def save(self):
        db.session.add(self)
        db.session.commit()

        return self
