from googleapiclient.discovery import build
import os, sys

REMOVE = 'The Nature of Code'
NAME = '11: Neuroevolution'
ID = 'PLRqwX-V7Uu6Yd3975YwxrR0x40XGJ_KGO'
API_KEY = 'AIzaSyAuQpsmRRbJgd-0pktJ0bjP8dSwGjVL6rY'
PATH = r'E:\Software\GitHub Desktop\website\_more\archive\nature-of-code'

NAME = NAME.replace(': ', '-').replace(' ', '-')
def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
	    enc = file.encoding
	    if enc == 'UTF-8':
	        print(*objects, sep=sep, end=end, file=file)
	    else:
	        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
	        print(*map(f, objects), sep=sep, end=end, file=file)

if __name__ == '__main__':
	os.chdir(f'{PATH}')
	os.makedirs(f'{NAME}')
	os.chdir(f'{PATH}/{NAME}')

	youtube = build('youtube', 'v3', developerKey=API_KEY)

	items = youtube.playlistItems().list(
				part = 'contentDetails, snippet',
				playlistId=ID,
				maxResults=50
				)

	pl_items = items.execute()
	# uprint(pl_items)

	for i,item in enumerate(pl_items['items']):
		vid_id = item['contentDetails']['videoId']
		# print(vid_id,end='\n\t')
		vid_req = youtube.videos().list(
					# part = 'contentDetails',
					part = 'snippet',
					id = vid_id
				)
		details = vid_req.execute()['items'][0]['snippet']
		# uprint(details)
		file_name = details['title'].replace('I.', '0.').replace('?', "").replace(REMOVE, "").replace(': ', '-').replace(' - ', '-').replace(' ', '-')[0:-1]
		# print(file_name, end='\n\t')

		title = ' '.join(file_name.split('-')[1:])
		title = title.replace(REMOVE, "")
		# print(title, end='\n')
		video_number = i+1
		date = details['publishedAt'][0:10]
		video_id = vid_id
		for line in details['description'].split('\n'):
			if "This video" or 'this video' in line:
				description = line
				break
		with open(f'{file_name}.md', 'w') as f:
			f.writelines('---\n')
			f.writelines(f'title: {title}\n')
			f.writelines(f'video_number: {video_number}\n')
			f.writelines(f'date: {date}\n')
			f.writelines(f'video_id: {video_id}\n')
			f.writelines('---\n')
			f.writelines(f'{description}\n')



		# uprint(details['publishedAt'][0:10], end='\n\t')
		# uprint(details['title'].replace(': ', '-').replace(' - ', '-').replace(' ', '-'), end='\n\t')
		# uprint(details['description'].split('\n')[0], end='\n\t')
		# print()


