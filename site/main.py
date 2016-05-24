import requests
import json
from urllib2 import urlopen
import time

url = "http://127.0.0.1:5000"
headers = {'Content-Type': 'application/json'}


def post_public_ip():
    global url
    global headers

    try:
        my_ip = urlopen('http://ip.42.pl/raw').read()
        # my_ip.encode("ascii", "ignore")
        my_ip = {"addr": my_ip}
        requests.post(url + "/sites/site/report",
                      headers=headers,
                      data=json.dumps(my_ip))
    except Exception, e:
        print str(e)


if __name__ == "__main__":
    while (1):
        post_public_ip()
        time.sleep(600)
