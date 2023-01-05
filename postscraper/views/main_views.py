from flask import Blueprint, render_template, request
from postscraper.scraper import naverscraper

bp = Blueprint('main', __name__, url_prefix='/')  # main은 별칭


# url_prefix -> localhost:500/ 만약 '/main'이라면 localhost:5000/main/


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/result', methods=['POST', 'GET'])
def create(url=None):
    if request.method == 'POST':
        value = request.form['content']
        url = str(value)
        post = naverscraper.getNaverBlogPost(url)
        return render_template('result.html', post=post)
    elif request.method == 'GET':
        url = request.args.get('url')
        post = naverscraper.getNaverBlogPost(url)
        return render_template('index.html', post=post)