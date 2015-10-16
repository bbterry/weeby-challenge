from flask import Flask, request, render_template

app = Flask(__name__)


@app.after_request
def after(response):
    if request.method == "GET":
        response.headers["Access-Control-Allow-Origin"] = "*"
    return response

@app.route('/')
def index():
    return 'Index Page'	

@app.route('/weeby/magic', methods=['GET'])
def hello_world():
    # Happy hacking :)
	if request.method == 'GET':
		input = request.args.get('spell', '')
		result = ""
		dict = {"xyzzy":"fred", "fred":"quux", "quux":"xyzzy"}
		while(input != ""):
			if(len(input) >= 4) and (input[0:4] in dict):
				result += dict.get(input[0:4])
				input = input[4:]
			elif(len(input) >= 5) and (input[0:5] in dict):
				result += dict.get(input[0:5])
				input = input[5:]
			else:
				return "Invalid Input!"
		return result
	return "Invalid Input!"

@app.route('/weeby/key.css', methods=['GET'])
def display_key():
	if request.method == 'GET':
		return render_template('key.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)	
