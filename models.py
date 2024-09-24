from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


# MODELS GO BELOW!
class Pet(db.Model):
    """Pet."""
    __tablename__ = 'pets'

    @classmethod
    def get_by_species(cls, species):
        return cls.query.filter_by(species=species).all()
    
    @classmethod
    def get_all_hungry(cls):
        return cls.query.filter(Pet.hunger > 20).all()

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

    def greet(self):
        """Greet using the pet's name and species."""
        return f"Hi, I'm {self.name} the {self.species}!"
    
    def feed(self, amt=10):
        self.hunger -= amt
        self.hunger = max(self.hunger, 0)
        
        db.session.add(self)
        db.session.commit()

        return 

