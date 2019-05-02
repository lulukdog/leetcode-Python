
if __name__ == '__main__':
	from collections import OrderedDict
	d = OrderedDict()

	nums = int(raw_input())
	# d = {}
	for i in range(nums):
		s = raw_input()
		d.setdefault(s,0)
		d[s] += 1

	res = ''
	print len(d)
	for i in d:
		res += str(d[i]) +' '

	print res[:-1]
