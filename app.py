from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_shop_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def list_pets():
    """List pets in db."""
    petList = Pet.query.all()
    return render_template('list.html', pets=petList)

@app.route('/<int:pet_id>')
def show_pet(pet_id):
    """Show details about a pet."""
    return render_template('details.html', pet=Pet.query.get_or_404(pet_id))

@app.route('/', methods=['POST'])
def add_pet():
    """Add a pet to the db."""
    name = request.form['name']
    species = request.form['species']
    hunger = request.form['hunger']
    hunger = int(hunger) if hunger else None

    newPet = Pet(name=name, species=species, hunger=hunger)
    db.session.add(newPet)
    db.session.commit()

    return redirect(f'/{newPet.id}')

@app.route('/species/<string:species>')
def show_species(species):
    """Show pets of a species."""
    pets = Pet.get_by_species(species)
    return render_template('species.html', pets=pets, species=species)