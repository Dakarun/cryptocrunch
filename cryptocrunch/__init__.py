from flask import Flask
from flask_apscheduler import APScheduler

from cryptocrunch import db
from cryptocrunch.config import Config


app = Flask(__name__)
app.config.from_object(Config())

scheduler = APScheduler()


@scheduler.task('interval', id='test_print', seconds=2, misfire_grace_time=900)
def test_print():
    with open('text.txt', 'a') as f:
        from datetime import datetime
        f.write(datetime.now().isoformat())
        f.write('\n')
    print('Job fired')


@app.route('/')
def hello_world():
    return '<p>Hello, worlds</p>'


if __name__ == '__main__':
    db.init_app(app)
    scheduler.init_app(app)
    scheduler.start()
    app.run()
