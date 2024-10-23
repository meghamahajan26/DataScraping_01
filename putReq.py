import requests as rq

qHeaders = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

put_data = {
    'name': 'M.Mahajan',
    'job': 'Data Analyst'
}

put_resp = rq.put(url='https://httpbin.org/put', headers=qHeaders, data=put_data)

if put_resp.status_code == 200:
    print('PUT successful:', put_resp.json())
else:
    print('PUT failed')
