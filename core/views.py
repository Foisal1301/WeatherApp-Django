from django.shortcuts import render
import json
import urllib.request

def index(request):
	data = {}
	if request.method == "POST":
		city = request.POST['city']
		if city.count(" ") != 0:
			city = city.replace(" ","+")
		try:
			res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=0263d3639e512a293643f87b2bd02e4d').read()
			json_data = json.loads(res)
			data = {
				'city':json_data['name'],
				"country_code":str(json_data['sys']['country']),
				"coordinate":str(json_data["coord"]["lon"])+ " "+str(json_data["coord"]["lat"]),
				"temp":str(round(json_data["main"]["temp"]-273,2))+"°C",
				"pressure":str(json_data['main']['pressure']),
				"humidity":str(json_data['main']['humidity']),
			}
		except:
			data['errors'] = "\""+request.POST['city']+"\" is not Found"

	return render(request,"core/index.html",{
			'data':data,
		})