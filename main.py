import requests
import json
import schedule
import time

def send_api():
    API_HOST = "https://hooks.slack.com"
    PATH = "/services/T060YSW91L2/B061210V41K/RQIi384ioqKelTLyqOuOnCzo"
    URL = API_HOST + PATH
    print(URL)
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    body = {
        "text": '<!everyone>' + "\n 1. 이번 주 달성할 Key Result는 무엇인가요?\n 2. 달성을 위해 오늘 할 일은 무엇인가요?\n 3. 그 외 논의할 것은?"
    }


    try:
        response = requests.post(URL, headers=headers, data=json.dumps(body))
        print(response)
        print(response.text)
    except Exception as e:
        print(e)


schedule.every().monday.at("09:00").do(send_api)
schedule.every().tuesday.at("09:00").do(send_api)
schedule.every().wednesday.at("09:00").do(send_api)
schedule.every().thursday.at("09:00").do(send_api)
schedule.every().friday.at("09:00").do(send_api)

if __name__ == "__main__":
    print("run slack todo workflow scheduler")
    while True:
        schedule.run_pending()