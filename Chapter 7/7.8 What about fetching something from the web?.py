import urllib.request

url = "https://www.w3.org/TR/PNG/iso_8859-1.txt"
destination_filename = "somefile.txt"

urllib.request.urlretrieve(url, destination_filename)

with open("somefile.txt") as f:
    content = f.read()

words = content.split()
print(f"There are {len(words)} words in the file.")

#####
import requests

r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
r.status_code # 200
r.headers['content-type'] # 'application/json; charset=utf8'
r.encoding # 'utf-8'
r.text # '{"type":"User"...'
r.json() # {'private_gists': 419, 'total_private_repos': 77, ...}