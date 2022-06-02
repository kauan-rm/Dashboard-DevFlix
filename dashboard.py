from app import create_app, db
from app.models import *
from flask_migrate import Migrate

app = create_app("default")
#app = create_app()

migrate = Migrate(app,db)

if __name__ == "__main__":
    app.run(debug=True)