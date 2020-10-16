import os, sys

PATH = r'E:\Software\GitHub Desktop\website\_more\archive\nature-of-code'

if __name__ == '__main__':
	os.chdir(f'{PATH}')
	for filename in os.listdir(PATH):
	    print(filename)