import requests as rq

qHeaders = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

post_data = {
    'name': 'Riya',
    'job': 'developer'
}

post_resp = rq.post(url='https://httpbin.org/post', headers=qHeaders, data=post_data)

if post_resp.status_code == 200:
    print('POST successful:', post_resp.json())
else:
    print('POST failed')
