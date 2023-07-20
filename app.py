import datetime
import locale
import io
import requests
import logging
import hashlib
import base64
import urllib.parse
from flask import Flask, render_template, send_file, jsonify, request, abort
from browser import make_screenshot

from weather import weather_code_to_info

locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")

METEO_TOKEN = "685db9ef151cc658e2d46520e693bdc553f516c2b6872a1951acb7e89954d5c7"  # noqa: E501
INSEE_CHAMPS_SUR_MARNE = 77083

API_ROUTE = "https://api.meteo-concept.com/api"
API_DAILY = "/forecast/daily"
API_NEXT_HOURS = "/forecast/nextHours"


CACHE_DURATION = datetime.timedelta(hours=1)

WEBSITES = [
    "https://weathermap.opengate.space",
    "https://screen.opengate.space/clock",
    "http://monitoring.mgmt.opengate.space:3000/dashboard/snapshot/w6OlhdMnrWpaWuCiNrSAusvA55G9mGPc?orgId=1&refresh=1m&from=now-1h&to=now",
]


last_weather_refresh: datetime.datetime = datetime.datetime.min
last_image_refresh: datetime.datetime = datetime.datetime.min

weather_cache = {}


app = Flask(__name__)

logger = logging.getLogger('waitress')
logger.setLevel(logging.INFO)


def get_weather_data() -> dict:
    global last_weather_refresh
    global weather_cache

    if last_weather_refresh + CACHE_DURATION < datetime.datetime.now():
        req = requests.get(API_ROUTE + API_NEXT_HOURS, params={
            'token': METEO_TOKEN,
            'insee': INSEE_CHAMPS_SUR_MARNE
        },
            headers={'Accept': 'application/json'}
        )
        logger.info(str(datetime.datetime.now()) + ' Refresh weather')
        weather_cache = req.json()
        last_weather_refresh = datetime.datetime.now()
    return weather_cache


def transform_weather_data(weather_data: dict) -> tuple:
    forecast = weather_data["forecast"]
    image, weather = weather_code_to_info(forecast[0]['weather'])
    actual = {
        'temp': forecast[0]['temp2m'],
        'rain': forecast[0]['probarain'],
        'humidity': forecast[0]['rh2m'],
        'wind': forecast[0]['wind10m'],
        'image': image,
        'weather': weather,
    }

    future = []
    for i in range(1, 4):
        date: str = datetime.datetime.fromisoformat(forecast[i]['datetime'])
        image, weather = weather_code_to_info(forecast[i]['weather'])
        future.append(
            {
                'date': date,
                'temp': forecast[i]['temp2m'],
                'image': image,
                'weather': weather,
            }
        )

    return tuple([actual, future])


@app.route("/")
def index():
    return render_template(
        'index.html',
        now=datetime.datetime.now()
    )


@app.route("/image_list")
def imageList():

    return jsonify(["/screenshot?url=" + urllib.parse.quote(website) + "&date=" +
                   datetime.datetime.now().strftime("%m%d%Y%H%M") for website in WEBSITES])


@app.route("/screenshot")
def screenshot():
    if request.args.get('url') not in WEBSITES:
        abort(404)
    return send_file(
        io.BytesIO(
            make_screenshot(
                request.args.get('url'),
                request.args.get('date'))),
        mimetype='image/jpeg',
        as_attachment=True,
        download_name='%s.jpg' %
        image_name)


@app.route("/clock")
def clock():
    weather = get_weather_data()
    actual_weather, forecast_weather = transform_weather_data(weather)
    return render_template(
        'clock.html',
        actual_weather=actual_weather,
        forecast_weather=forecast_weather,
        now=datetime.datetime.now()
    )


image: bytes = b''
image_name: str = ""


@app.route("/image")
def get_image():
    global image, image_name, last_image_refresh

    if last_image_refresh + CACHE_DURATION < datetime.datetime.now():
        req = requests.get("https://source.unsplash.com/1980x1080/?space")
        image = req.content
        image_name = base64.b64encode(hashlib.sha256(image).digest()).decode()
        logger.info(str(datetime.datetime.now()) + ' Refresh image')
        last_image_refresh = datetime.datetime.now()

    return send_file(
        io.BytesIO(image),
        mimetype='image/jpeg',
        as_attachment=True,
        download_name='%s.jpg' % image_name)
