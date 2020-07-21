import time
from flask.cli import FlaskGroup
from project import create_app
from project.model.model import User

app = create_app()

cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
	try:
		app.db.drop_all()
		app.db.create_all()
		app.db.session.commit()
		print('DB created !')
	except Exception as e:
		print('Create DB Error!')
		print(e)
    
@cli.command("seed_db")
def seed_db():
	try:
		user = User(email="gabriel@mail.com",
		username="gabriel00",
		password="senha123")
		user.gen_hash()

		app.db.session.add(user)
		app.db.session.commit()
	except Exception as e:
		print('seed db Error!')
		print(e)

if __name__ == "__main__":
    cli()