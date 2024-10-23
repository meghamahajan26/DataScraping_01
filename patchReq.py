import requests as rq

qHeaders = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

patch_data = {
    'job': 'Sr. Data Analyst'
}

patch_resp = rq.patch(url='https://httpbin.org/patch', headers=qHeaders, data=patch_data)

if patch_resp.status_code == 200:
    print('PATCH successful:', patch_resp.json())
else:
    print('PATCH failed')
