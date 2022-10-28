import urllib.request

url = "https://www.baidu.com"

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.Request(request)

content = response.read().decode('utf8')

print(content)
