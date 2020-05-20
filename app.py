from sqlalchemy import create_engine
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    engine = create_engine('postgresql://postgres:8426dharM4@localhost:5432')
    units = engine.execute('select * from unittype').fetchall()
    print(units)
    return 'Success'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
