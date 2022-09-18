def func(mylist):

  for i in range(0,len(mylist)):
    for j in range(i+1,len(mylist)):
      if mylist[i] == mylist[j]:
        return mylist[i] 
  return 0

def hashtable(mylist):
  mydict = {}
  for i in range(0,len(mylist)):
    if mylist[i] in mydict:
      return mylist[i]
    else:
      mydict[mylist[i]]=i
  return 0
  
# def hash(mylist):
#   d = {}
#   d = {x: mylist.count(x) for x in mylist}
#   return d
# output : {2: 2, 1: 2, 3: 1, 4: 1, 5: 1}

def hash(mylist):
  d = {}
  for i in range(len(mylist)):
    if mylist[i] in d:
      return mylist[i] 
    else:
      d[mylist[i]] = i
  return 0

mylist = [2,1,1,2,3,4,5]
x = hash(mylist)
print(x)
y = hashtable(mylist)
print(y)