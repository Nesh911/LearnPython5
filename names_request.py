import requests


def get_names(url):
    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    else:
        print("ой")


if __name__ == "__main__":
    data = get_names("https://apidata.mos.ru/v1/datasets/2009/rows?api_key=c0247fff6c7ea608f20f8edacd8cdc57")
    print(data)