from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Index page"""
    return render_template('index.html')

@app.route('/blog/')
def blog():
    """Blog page"""
    return render_template('blog.html')

@app.route('/faq/')
def faq():
    """FAQ page"""
    return render_template('faq.html')

if __name__ == '__main__':
    app.run(debug=True)
