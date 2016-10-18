import requests
title_text = input("enter a title search string ")
url = 'http://www.omdapi.com/?=&plot=short&r=json&s={}'.format(title_text)

resp = requests.get(url)
if resp.status_code != 200:
    print("status code unexpected {}".format(resp.status_code))
else:
    search_data  = resp.json()['Search']
    for m in search_data:
        print("* {}".format(m['title']))
