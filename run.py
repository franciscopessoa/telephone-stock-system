from app import app, db
from flask.cli import FlaskGroup
from app.models.user import User

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    userAdmin = User(username="admin", password="usH5hRwxiZ", name="Admin", email="admin@email.com")
    userAdmin.hash_password();
    db.session.add(userAdmin)
    db.session.commit()


if __name__ == "__main__":
    cli()
