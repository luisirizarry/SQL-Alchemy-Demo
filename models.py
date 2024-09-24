from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


# MODELS GO BELOW!
class Pet(db.Model):
    """Pet."""
    __tablename__ = 'pets'

    def __repr__(self):
        p = self
        return f"<Pet id={p.id} name={p.name} species={p.species} hunger={p.hunger}>"

    id = db.Column(db.Integer, 
                   primary_key=True, 
                   autoincrement=True)
    
    name = db.Column(db.String(50), 
                     nullable=False,
                     unique=True)
    
    species = db.Column(db.String(30), nullable=False)

    hunger = db.Column(db.Integer, default=20)
