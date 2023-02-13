from models import *

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Add Pets
woofly = Pet(name='Woofly', species='Dog', photo_url='https://images.unsplash.com/photo-1600804340584-c7db2eacf0bf?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NXx8cHVwcHl8ZW58MHx8MHx8&w=1000&q=80', age=1, available=False)
porchetta = Pet(name='Porchetta', species='Porcupine', photo_url='https://southwickszoo.com/wp-content/uploads/IMG_3811-scaled-e1618596407899.jpg', age=2)
snargle = Pet(name='Snargle', species='Cat', photo_url='https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/1200px-Cat03.jpg', age=3)

# Add new objects to session
db.session.add_all([woofly, porchetta, snargle])

# Commit data to db
db.session.commit()