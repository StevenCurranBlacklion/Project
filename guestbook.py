from flask import Flask, render_template, request, send_file
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
	
@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/click') 
def name():         
	return 'Thanks for signing our guestbook! Have a good day!'

@app.route('/process', methods=['POST'])
def process():
	name = request.form['name']
	comment = request.form['comment']

	return render_template('index.html', name=name, comment=comment)

if __name__ == '__main__':
	app.run(debug=True)