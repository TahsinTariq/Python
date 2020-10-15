from googleapiclient.discovery import build
import os, sys

NAME = '1-Vectors-The-Nature-of-Code'
ID = 'PLRqwX-V7Uu6ZwSmtE13iJBcoI-r4y7iEc'
API_KEY = 'AIzaSyAuQpsmRRbJgd-0pktJ0bjP8dSwGjVL6rY'
PATH = r'E:\Software\GitHub Desktop\website\_more\archive\nature-of-code'


def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
	    enc = file.encoding
	    if enc == 'UTF-8':
	        print(*objects, sep=sep, end=end, file=file)
	    else:
	        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
	        print(*map(f, objects), sep=sep, end=end, file=file)

if __name__ == '__main__':
	youtube = build('youtube', 'v3', developerKey=API_KEY)

	items = youtube.playlistItems().list(
				part = 'contentDetails, snippet',
				playlistId=ID,
				maxResults=50
				)

	pl_items = items.execute()
	uprint(pl_items)

	# for item in pl_items['items']:
	# 	vid_id = item['contentDetails']['videoId']
	# 	print(vid_id,end='\n\t')
	# 	vid_req = youtube.videos().list(
	# 				# part = 'contentDetails',
	# 				part = 'snippet',
	# 				id = vid_id
	# 			)
	# 	details = vid_req.execute()['items'][0]['snippet']
	# 	# uprint(details)
	# 	uprint(details['publishedAt'][0:10], end='\n\t')
	# 	uprint(details['title'], end='\n\t')
	# 	uprint(details['description'].split('\n')[0], end='\n\t')
	# 	print()


