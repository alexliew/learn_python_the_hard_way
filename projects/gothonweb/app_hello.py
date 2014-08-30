from flask import Flask, render_template, request
import logging

app = Flask(__name__)
app.config['trim_blocks'] = True
app.config['lstrip_blocks'] = True

@app.route('/hello', methods=['POST', 'GET'])
def hello():
    if request.method == 'POST':
        name = request.form.get('name', 'Nobody')
        greeting = request.form.get('greet', 'Hello')
        return render_template('hello_block.html', name=name, greeting=greeting)
    elif request.method == 'GET':
        return render_template('hello_form_block.html')

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
