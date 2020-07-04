import praw
# import urllib.request
import requests

# p = {'http': 'https://222.39.8.103:8118'}
reddit = praw.Reddit(client_id='vKBEy1Rw-fegKA',
                     client_secret='TBLBGwcDK24LmfizbtqNsjFq38g',
                     username='fatty_mcsquirrelface',
                     password='fattyfatfatso',
                     user_agent='fatty_mcsquirrelfaceLOL')
                     # HTTPS_PROXY='https://222.39.8.103:8118')

# print(urllib.request.urlopen("http://httpbin.org/ip", proxies=p).read())
# print(requests.get("http://httpbin.org/ip", proxies=p))
# print(requests.get("http://httpbin.org/ip", stream = True))
# with requests.get("http://httpbin.org/ip", stream=True) as r:
#     print(r._original_response.fp._sock.getpeername()[0])
sub = reddit.subreddit('mildlyinteresting')
posts = sub.hot(limit=5)
for post in posts:
    print(post.title)
    print('\n\n')
exit()
