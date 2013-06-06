import urllib, json
search = urllib.urlopen("http://search.twitter.com/search.json?q=" + 'python')
dic = json.loads(search.read())
print dic["results"][0]["text"]
