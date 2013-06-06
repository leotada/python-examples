import urllib
import json


def searchTweets(query):
    search = urllib.urlopen("http://search.twitter.com/search.json?q="+query)
    dic = json.loads(search.read())
    for result in dic["results"]: # result is a list of dictionaries
        print "*",result["text"],"\n"

searchTweets("python")
