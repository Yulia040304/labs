from app import db

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    difficulty = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Recipe {self.name} {self.model}"
