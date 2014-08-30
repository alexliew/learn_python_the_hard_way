from flask import Flask, render_template, request, session, redirect, url_for, flash
import logging
import pickle

from gothonweb import map

app = Flask(__name__)
app.config['trim_blocks'] = True
app.config['lstrip_blocks'] = True
app.secret_key = b"\xf5\xec'w\xd7\xb6\xb3\x82x.\x94\xf6\xb3\x98\xbe\x1e\xd8Vtw\xbc2\x04\xfa"

@app.route('/game', methods=['POST', 'GET'])
def gameEngine():
    if request.method == 'GET':
        if session['room']:
            rm = pickle.loads(session['room'])
            if session.get('invalid', False):
                flash("We did not understand you.", 'error')
            return render_template('show_room.html', room=rm)
        else:
            # why is this here? do you need it?
            return render_template('you_died.html')
    elif request.method == 'POST':
        action = request.form.get('action', None)
        if session['room'] and action:
            rm = pickle.loads(session['room'])
            new_rm = rm.go(action)
            if new_rm == rm:
                session['invalid'] = True
                # flash("What you say?")
            else:
                session['room'] = pickle.dumps(new_rm)

        return redirect(url_for('gameEngine'))

@app.route('/')
def index():
    # this is used to "setup" the session with starting values
    session['room'] = pickle.dumps(map.START)
    return redirect(url_for('gameEngine'))

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
