from flask import Flask, request, render_template, jsonify, json, session
import math

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
		
@app.route('/weeby/flappy', methods=['POST'])
def flappy():
	if request.method == 'POST':
		data = request.get_json()
		wallNo = 0 #next wall I am going to pass through
		count = 0 
		while count < len(data['walls']):
			#To check where am I and which is the next wall
			if data['me']['x'] >= data['walls'][count]['x']+data['walls'][count]['w']: 
				wallNo = count + 1
			count += 1
		t_base = data['t'] #absolute time
		distance = data['walls'][wallNo]['x'] + data['walls'][wallNo]['w'] - data['me']['x'] #distance from me to wall
		timeToWall = round(distance / data['me']['vx']) #time needed to fly from me to wall 
		hToGap = data['me']['y'] - data['walls'][wallNo]['gaps'][0]['y'] #The vertical distance from me to the bottom of the gap
		g = data['grav'] #gravity
		vt = data['thrust'] #thrust speed
		vy = data['me']['vy'] # my speed
		queue = [] #list of time to flap
		t = 0 #relative time
		#I am higher than the bottom of the gap
		if hToGap > 0:
			#I am flying up
			if vy >= 0:
				t = int(vy / g + math.sqrt(vy * vy / (g * g) + 2 * hToGap / g)) #calculate the time when I can get to the height of the bottom of the gap
				queue.append(t_base + t)
			#I am dropping down
			else:
				t = int(quadratic_equation(g / 2, vy, hToGap)) #calculate the time when I can get to the height of the bottom of the gap
				queue.append(t_base + t)
			t += round(2 * vt / g) #this is the next time when I reach the height of the bottom of the gap
		#I am lower than the bottom of the gap
		else:
			#keep flap every unit time until higher than the bottom of the gap
			while hToGap < 0:
				t += 1
				queue.append(t_base + t)
				hToGap += vt - g / 2
			t += int(vt / g + math.sqrt((vt - g) * (vt - g) / (g * g) + 2 * hToGap / g)) #this is the next time when I reach the height of the bottom of the gap
		#keep myself higher than the bottom of the gap
		while t <= timeToWall:
			queue.append(t_base + t)
			t += round(2 * vt / g)
		t -= round(vt / g) #this is the time when I reach the highest point of going up
		return jsonify(queue = queue, next = t_base + t)

#This function is to solve the quadratic equation with one unknown
def quadratic_equation(a,b,c):
    delta = b*b - 4*a*c
    if delta < 0:
        return 0
    elif delta == 0:
        return -(b/(2*a))
    else:
        sqrt_delta = math.sqrt(delta)
        x1 = (-b + sqrt_delta)/(2*a)
        x2 = (-b - sqrt_delta)/(2*a)
        return (x1 if x1 > x2 else x2)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)	
	
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
