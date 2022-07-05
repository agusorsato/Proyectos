import requests
import json
from datetime import datetime

class API:
    def getData(self):
        url = "https://weatherapi-com.p.rapidapi.com/current.json"

        querystring = {"q":"Cordoba"}
        fecha = datetime.now()
        fecha = fecha.strftime("%Y-%m-%d-%H%M%S")

        headers = {
            "X-RapidAPI-Key": "d24a33d61fmsh9186add7626b7e8p1a8d78jsnbf7d9b2f0f92",
            "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        # Creamos un archivo con el nombre de la ciudad
        with open(querystring["q"] + fecha + ".json", "w") as f:
                ##transformamos la respuesta en un json con dic
                 json.loads(response.text)
                 f.write(response.text)