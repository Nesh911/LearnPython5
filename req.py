import requests


def get_weather(url):
    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    else:
        print("ой")


if __name__ == "__main__":
    data = get_weather("http://api.openweathermap.org/data/2.5/weather?id=524901&APPID=005004cb35286608ce5c4e02ab2f9d64&units=metric")
    print(data)



    # https://apidata.mos.ru/v1/datasets/2009/rows?api_key=c0247fff6c7ea608f20f8edacd8cdc57