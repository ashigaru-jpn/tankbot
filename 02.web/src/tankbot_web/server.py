# Sumobot server with flask

from flask import Flask, render_template, request
from gpio import MotorDriver

# Flask start
app = Flask(__name__)
md = MotorDriver()

# server_run
def server_run(host, port, pin_right_1, pin_right_2, pin_left_1, pin_left_2):
	# MUST execute before app.run
	md.setPin(pin_right_1, pin_right_2, pin_left_1, pin_left_2)
	# always last
	app.run(host=str(host), port=int(port))

# route index
@app.route('/')
def show_index():
    return render_template('index.html')

# route action with post
@app.route('/action', methods=['POST'])
def action():
    if request.method == 'POST':
        do_post()
    return ''

# route status with get
@app.route('/status', methods=['GET'])
def status():
	ret = ''
	if request.method == 'GET':
		ret = do_get()
	return ret

# do post method
# get parameter, and control LED or Servo
def do_post():
        type = str(request.form['type'])
        val = str(request.form['value'])
        if type == 'gpio':
                md.command(val)

# do get method
# return button status
def do_get():
	status = 1
	json = "{\"status\":%d}" %(status)
	return json

# end of flask
