import urllib
import json

# Authentication:
import oauth2 as oauth
import time

# API endpoint
url = "https://api.twitter.com/1.1/search/tweets.json?q=twitter&count=50&result_type=popular"


consumer = oauth.Consumer(key="brzlQSmBD0kA9xQQepsaAw", secret="MYkREfL038U7vImBeHetXD5KRHjnMqgmh0EX9EVLGs")
#request_token_url = "https://api.twitter.com/oauth/request_token"
token = oauth.Token(key="316597352-btdrCWSPUDMnBoxZKeUsnSQtGxgSCcrGKm4e9L1q", secret="4LRq78oVpfzdqTWSw8t4uU9zGI6hJVpfKc95ZFpCk")
client = oauth.Client(consumer, token)
 

resp, content = client.request(url, "GET")
# print resp
result_list =  json.loads(content)['statuses']
for res in result_list:
  print res['text']
# [0]['text']
# response = urllib.urlopen("")
# print json.load(response)
