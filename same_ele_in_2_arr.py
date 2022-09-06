# arr1 = list(map(int, input().split()))
# arr2 = list(map(int, input().split()))
# for i in arr1:
#   for j in arr2:
#     if i == j:
#         print(True)
# print(False)

# # from os import system
# # system("python same_ele_in_2_arr.py") system("python same_ele_in_2_arr.py")


arr1 = list(map(str,input().split()))
arr2 = list(map(str,input().split()))
d1 = {x : arr1.count(x) for x in arr1}
for i in arr2:
  if i in d1.keys():
    print(True)
print(False)


for i in arr2:
  if arr1.find(i):
    print (True)