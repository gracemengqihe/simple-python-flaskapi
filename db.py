
from application import app
from application import db
from application import Drink

app.app_context().push()
db.create_all()
drink1 = Drink(name = 'carrot juce', description = 'Tastes like carrots')
drink2 = Drink(name = 'orange juce', description = 'Tastes like orange')
drink3 = Drink(name = 'grape juice', description = 'Tastes like grape')

db.session.add(drink1)
db.session.add(drink2)
db.session.add(drink2)
db.session.commit()

