from googleapiclient.discovery import build

api_key = 'AIzaSyAuQpsmRRbJgd-0pktJ0bjP8dSwGjVL6rY'

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(
			part = 'contentDetails,statistics',
			# forUsername='shiffman'
			forUsername='enyay'
			)
print(request.execute()['items'])
# url = request.execute()['items'][0]['id']
# playlist = youtube.playlists().list(
# 			part = 'contentDetails, snippet',
# 			channelId=url
# 			)
# print(playlist.execute())