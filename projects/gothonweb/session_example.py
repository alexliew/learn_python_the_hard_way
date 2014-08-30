from flask import Flask, render_template, request, session
import logging

app = Flask(__name__)
app.config['trim_blocks'] = True
app.config['lstrip_blocks'] = True
app.secret_key = b"\xf5\xec'w\xd7\xb6\xb3\x82x.\x94\xf6\xb3\x98\xbe\x1e\xd8Vtw\xbc2\x04\xfa"

@app.route('/count', methods=['POST', 'GET'])
def count():
    session['count'] = session.get('count', 0) + 1
    return str(session['count'])

@app.route('/reset')
def reset():
    session.clear()
    return ""

# def config():
#     logging.basicConfig(filename="log/app.log",
#                         level=logging.DEBUG)
#     # define a handler which writes INFO messages and above
#     console = logging.StreamHandler()
#     console.setLevel(logging.INFO)
#     # set a format which is simpler for console use
#     formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
#     # tell the handler to use this format
#     console.setFormatter(formatter)
#     #add the handler to the root logger
#     logging.getLogger('').addHandler(console)

if __name__ == "__main__":
    app.run(debug=True)
