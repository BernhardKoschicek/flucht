from flask import Blueprint, abort, current_app, g, redirect, render_template, \
    request, url_for
from flask_babel import _

from flucht import app
from flucht.data.logos import logos
from flucht.data.references import intro_books
from flucht.util.build_img_tag import build_img_tag, build_modal_img
from flucht.util.build_newspaper_tag import build_modal_newspaper, \
    build_newspaper_tag
from flucht.util.pages import get_sections_pages

multilingual = Blueprint(
    'multilingual',
    __name__,
    template_folder='templates',
    url_prefix='/<lang_code>')


@multilingual.url_defaults
def add_language_code(endpoint, values):
    values.setdefault('lang_code', g.lang_code)


@multilingual.url_value_preprocessor
def pull_lang_code(endpoint, values):
    g.lang_code = values.pop('lang_code')


@multilingual.before_request
def before_request():
    if g.lang_code not in current_app.config['LANGUAGES']:
        adapter = app.url_map.bind('')
        try:
            endpoint, args = adapter.match(
                '/en' + request.full_path.rstrip('/ ?'))
            return redirect(url_for(endpoint, **args), 301)
        except:
            abort(404)

    dfl = request.url_rule.defaults
    if 'lang_code' in dfl:
        if dfl['lang_code'] != request.full_path.split('/')[1]:
            abort(404)


@multilingual.route('/')
def intro() -> str:
    return render_template(
        'multilingual/intro.html',
        title=_('page_titel'),
        books=intro_books,
        images=build_img_tag())


@multilingual.route('/exhibition', defaults={'lang_code': 'en'})
@multilingual.route('/ausstellung', defaults={'lang_code': 'de'})
def exhibition():
    return render_template(
        'multilingual/exhibition.html',
        title=_('page_titel'),
        newspaper=build_newspaper_tag(),
        pages=get_sections_pages(),
        images=build_img_tag(),
        img_modal=build_modal_img(),
        news_modal=build_modal_newspaper(),
        sponsors=logos,
        )


@multilingual.errorhandler(404)
def page_not_found(e: Exception) -> tuple:
    return render_template('multilingual/404.html', e=e), 404


@app.route('/')
def index():
    g.lang_code = request.accept_languages.best_match(app.config['LANGUAGES'])
    return redirect(url_for('multilingual.intro'))
