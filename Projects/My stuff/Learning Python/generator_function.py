def fibb(n):
	i = -1
	j = 1
	for _ in range(n):
		result =  i + j
		i = j
		j = result
		yield j

if __name__ == '__main__':
	gen = fibb(10)
	d = {}
	for i in range(10):
		d[i] = 0
	# d[1] = d[1]+1
	# print(d)
	for i in gen:
		i = str(i)
		# print(i[0])
		for j in i:
			j = int(j)
			d[j] = d[j]+1

	print(sorted(d, key=lambda x: d[x]))

	# while True:
	# 	v = next(gen, None)
	# 	if v == None: break
	# 	print(v)

	# while True:
	# 	try:
	# 		print(next(gen))
	# 	except:
	# 		break