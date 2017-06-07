from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

page_header = '''
    <!doctype html>
    <html>
        <head>
            <title>Web Caesar</title>
            <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
        </head>
        <body>
            <h1>Web Caesar</h1>
'''

page_form = '''
            <form method='POST'>
                <label for='rotate'>Rotate by:</label>
                <input type='number' name='rotate' id='rotate' />
                <br />
                <textarea name='message' id='message'></textarea>
                <br />
                <input type="submit" value="Ceasar!">
            </form>
'''

page_footer = '''
        </body>
    </html>
'''

@app.route('/', methods=['POST'])
def encrypt_page():
    rot = int(request.form['rotate'])
    message = request.form['message']
    secret_message = rotate_string(message, rot)
    return '<h1>' + secret_message + '</h1>'

@app.route("/")
def index():
    return page_header + page_form + page_footer

app.run()
