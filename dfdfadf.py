a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
b = ['a','b', 'c','d', 'e', 'f', 'g', 'h', 'i','j']
c = []
start = 0

for i in range(1,5):
    c.append(a[start:start+i])
    c.append(b[start:start+i])
    start += start+1
print(c)
