def sherlockAndAnagrams(s):

	def check_anagrams(word1,word2):
		d = {}
		n = len(word1)
		for i in range(n):
			d.setdefault(word1[i],0)
			d.setdefault(word2[i],0)
			if word1[i] in d:
				d[word1[i]] += 1
			if word2[i] in d:
				d[word2[i]] -= 1

		for key in d:
			if d[key] != 0:
				return 0

		return 1

	n = len(s)
	res = 0
	for i in range(1,n):
		for j in range(0,n-i+1):
			w1 = s[j:j+i]
			for k in range(j+1,n-i+1):
				w2 = s[k:k+i]
				res += check_anagrams(w1,w2)

	return res


if __name__ == '__main__':
	print(sherlockAndAnagrams('abba'))
	
