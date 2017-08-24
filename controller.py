from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
    Index page
    :return: template
    """
    return render_template('index.html')


@app.route('/blog/')
def blog():
    """
    Blog page
    :return: template
    """
    return render_template('blog.html')


@app.route('/faq/')
def faq():
    """
    FAQ page
    :return: template
    """
    return render_template('faq.html')
