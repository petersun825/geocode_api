import geocoder, csv
from flask import Flask, jsonify, request




app = Flask(__name__)

locations=[]

# create a class for location
class address():
	def __init__(self, location=''):
		self.location=location
	
	def get_latlng(self):
		g = geocoder.arcgis(self.location)
		lat=str(g.latlng[0])
		lng=str(g.latlng[1])
		#convert latitude & longtitude into str and encapsulate with () 
		return "({0},{1})".format(lat,lng)



	# def write_header(self):
	# 	with open ('locations.csv', 'w') as csvfile:
	# 	fieldnames=['location', 'latitude', 'longtitude']
	# 	writer= csv.DictWriter(csvfile, fieldnames=fieldnames)
	# 	#header
	# 	writer.writeheader()

	# def write_location(self):
	# 	writer.writerow({'location': self.location, 'latitude': self.lat, 'longtitude': self.lng})


@app.route("/")
def index():
	pass
	
@app.route("/add_location/<location>", methods=["POST"])
def add_location(location):
	#I don't know why this needs to exist?
	data = request.get_json()

	#instantiate the class address with input of location, then assign to latlng
	new_latlng = address(location).get_latlng()

	new_location = {"location": location ,"latlng": new_latlng}
	locations.append(new_location)
	return jsonify ({ "status": "success", "locations": locations})

@app.route("/get_location/<location>", methods=["GET"])
def get_location(location):
	for place in locations:
		if place["location"]==location:
			return jsonify({"status": "success", "location": place})
	return jsonify({"error": "location not found"})

@app.route("/return_locations", methods=["GET"])
def return_locations():
	return jsonify({"locations": locations})
#main
if __name__ == "__main__":
	app.run(debug=True)





