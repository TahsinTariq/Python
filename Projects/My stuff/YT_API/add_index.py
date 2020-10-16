import os, sys

PATH = r'E:\Software\GitHub Desktop\website\_more\archive\nature-of-code'

if __name__ == '__main__':
	os.chdir(f'{PATH}')
	for filename in os.listdir(PATH):
		if filename != 'index.md':
			os.chdir(f'{PATH}/{filename}')
			fileTitle = " ".join(filename.split("-")[1:])
			series_number = filename.split("-")[0]
			print(fileTitle)
			# with open(f'index.md', 'w') as f:
			# 	f.writelines('---\n')
			# 	f.writelines(f'title: {fileTitle}\n')
			# 	f.writelines(f'series_number: {series_number}\n')
			# 	f.writelines(f'layout: series-index\n')
			# 	f.writelines('---\n')
			# 	f.writelines(f'These video lessons accompany Chapter {series_number} ({fileTitle}) from The Nature of Code book.\n')