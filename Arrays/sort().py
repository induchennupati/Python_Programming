from array import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
b=a.tolist()
b.sort()
a = arr.array('i')
a.fromlist(b)
print (a)