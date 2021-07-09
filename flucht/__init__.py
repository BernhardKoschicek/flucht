from flask import Flask, g, request
from flask_babel import Babel

app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config.default')  # type: ignore
app.config.from_pyfile('production.py')  # type: ignore

# import and register blueprints
from flucht.blueprints.multilingual import multilingual
app.register_blueprint(multilingual)

babel = Babel(app)


@babel.localeselector
def get_locale():
    if not g.get('lang_code', None):
        g.lang_code = request.accept_languages.best_match(app.config['LANGUAGES'])
    return g.lang_code


@app.before_request
def before_request():
    if request.path.startswith('/static'):
        return  # Only needed if not running with apache and static alias


@app.after_request
def apply_caching(response):
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response


# app.register_blueprint(filters.blueprint)

if __name__ == "__main__":  # pragma: no cover
    app.run()
