from json import dumps
from requests import post, get

url = "https://glados.rocks/api/user/checkin"
url2 = "https://glados.rocks/api/user/status"
useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"

def CheckIn(cookie):
    # referer = 'https://glados.space/console/checkin'
    origin = "https://glados.space"

    payload = {'token': 'glados.one'}

    checkin = post(
        url,
        headers={
            'cookie': cookie,
            # 'referer': referer,
            'origin': origin,
            'user-agent': useragent,
            'content-type': 'application/json;charset=UTF-8'
        },
        data=dumps(payload)
    )
    state = get(
        url2,
        headers={
            'cookie': cookie,
            # 'referer': referer,
            'origin': origin,
            'user-agent': useragent
        }
    )

    mess = checkin.json()['message']
    # time = state.json()['data']['leftDays']
    days = state.json()['data']['leftDays'].split('.')[0]
    # days = time.split('.')[0]
    # msg = f'checkin: {checkin.status_code} | state: {state.status_code}\n{mess}\n剩余天数：{days}天'

    checkin.close()
    state.close()

    # print(f'{mess}\n剩余天数:{days}天')

    return f'{mess}\n剩余天数:{days}天'
