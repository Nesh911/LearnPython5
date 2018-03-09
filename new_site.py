from flask import Flask, request
from req import get_weather
from datetime import datetime
from names_request import get_names

city_id = 524901
appid = "005004cb35286608ce5c4e02ab2f9d64"

app = Flask(__name__)


@app.route('/')
def index():
    url = "http://api.openweathermap.org/data/2.5/weather?id=%s&APPID=%s&units=metric" % (city_id,appid)
    weather = get_weather(url)
    cur_time = datetime.now().strftime('%d.%m.%Y')

    result = "<p><b>Температура: </b> %s\n</p>" % weather['main']['temp']
    result += "<p><b>Город: </b> %s</p>" % weather['name']
    result += "<p><b>Дата: </b>%s</p>" % cur_time
    return result


# @app.route('/names')
# def req_names():
#     global requested_year
#     url = "https://apidata.mos.ru/v1/datasets/2009/rows?api_key=c0247fff6c7ea608f20f8edacd8cdc57"
#     names = get_names(url)
#
#     result = '<table><tr><th> Имя</th><th> Год </th><tr>'
#     for i in names:
#         result += '<tr><td> %s </td>' % i['Cells']['Name']
#         result += '<td> %s </td>' % i['Cells']['Year']
#     result += '</tr></table>'
#     return result

# Получается только чтото одно, либо весь список, либо только с параметром...
@app.route('/names')
def req_names_arg():
    global requested_year
    url = "https://apidata.mos.ru/v1/datasets/2009/rows?api_key=c0247fff6c7ea608f20f8edacd8cdc57"
    names = get_names(url)
    years = [2015,2016,2017,2018]

    try:
        requested_year = int(request.args.get('year'))
    except (TypeError, ValueError):
        return "Ой"

    year = int(request.args.get('year')) if int(request.args.get('year')) in years else 0

    result = '<table><tr><th> Имя</th><th> Год </th><tr>'
    for i in names:
        if year == i['Cells']['Year']:
            result += '<tr><td> %s </td>' % i['Cells']['Name']
            result += '<td> %s </td>' % i['Cells']['Year']
        elif year == 0:
            result = "<p>Нет информации по запрошенному году</p>"

    result += '</tr></table>'
    return result


if __name__ == "__main__":
    app.run(port=5151)


