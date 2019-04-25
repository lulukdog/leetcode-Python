def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    uNum = n/k
    for i in range(uNum):
        s = list(string[k*i:k*(i+1)])
        l = list(set(s))
        l.sort(key = s.index)
        s = ''.join(l)
        print(s)


if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)
    