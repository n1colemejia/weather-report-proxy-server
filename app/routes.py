
from flask import Blueprint, request, jsonify
import os
from dotenv import load_dotenv
import requests

load_dotenv()

proxy_bp = Blueprint("proxy_bp", __name__)

location_key = os.environ.get("LOCATION_KEY")
weather_key = os.environ.get("WEATHER_KEY")

@proxy_bp.route("/location", methods=["GET"])
def get_lat_lon():
    loc_query = request.args.get("q")
    print("LOC QUERY", loc_query)
    if not loc_query:
        return {"message": "must provide q parameter (location)"}

    response = requests.get(
        "https://us1.locationiq.com/v1/search.php",
        params={"q": loc_query, "key": location_key, "format": "json"}
    )

    return jsonify(response.json())

@proxy_bp.route("/weather", methods=["GET"])
def get_weather():
    lat_query = request.args.get("lat")
    lon_query = request.args.get("lon")
    # print(request.args)
    print("lat_query: ", lat_query, "lon_query: ", lon_query)
    if not lat_query or not lon_query:
        return {"message": "must provide lat and lon parameters"}

    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather",
        params={
            "lat": lat_query,
            "lon": lon_query,
            "appid": weather_key,
            "units": "imperial"
            }
    )
    return response.json()

@proxy_bp.route("/forecast", methods=["GET"])
def get_forecast():
    lat_query = request.args.get("lat")
    lon_query = request.args.get("lon")
    # print(request.args)
    print("lat_query: ", lat_query, "lon_query: ", lon_query)
    if not lat_query or not lon_query:
        return {"message": "must provide lat and lon parameters"}

    response = requests.get(
        "https://api.openweathermap.org/data/2.5/forecast",
        params={
            "lat": lat_query, 
            "lon": lon_query, 
            "appid": weather_key,
            "units": "imperial"
            }
    )
    return response.json()