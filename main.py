from private.config import configure_resources
from flask import Flask
from sqlalchemy import create_engine

app = Flask(__name__)

@app.route("/")
def hw():
    return {"123": "123"}

if __name__ == '__main__':
    configure_resources()
    from private.config import config
    db = config['postgres']
    print(db)
    con = create_engine(f"{db['driver']}://{db['user']}:{db['password']}@localhost/{db['database']}")
    con.execute("SELECT * FROM films")
    app.run("0.0.0.0", port=5000)
