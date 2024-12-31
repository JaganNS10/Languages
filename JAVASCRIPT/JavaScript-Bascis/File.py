# N=14
# a=[12,7,5,1,13,1,10,8,11,9,2,4,3,6]
# Re = []
# Repeat=[]
# Missing=[]
# for i in range(len(a)):
#   if a[i] not in Re:
#     Re.append(a[i])
#   else:
#     Repeat.append(a[i])
# Missing=[i for i in range(1,len(a)+1) if i not in a]
# Repeat.extend(Missing)
# print(Repeat)

#another way
'''for i,j in enumerate(a):
  if i>0 and i not in a:
    Missing+=[i]
  count=a.count(j)
  if count>1 and j not in Repeat:
    Repeat.append(j)
if N not in a:
  Missing.append(N)
Result = Repeat+Missing
print(Result)'''
#subarray product
'''arr=[2,3,4,5,-1,0]

subarray=[]
for i in range(len(arr)):
  for j in range(i,len(arr)):
    subarray.append(arr[i:j+1])
Result=[]
for k in subarray:
  product=1
  for r in k:
    product=product*r
    Result.append(product)
print(max(Result))'''
#Both arrays are equal
'''a=[1,2,5,4,0]
b=[2,4,5,0,1]
count=0
for i,j in zip(sorted(a),sorted(b)):
  if i==j:
    count=count+1
if count==len(a):
  print(True)
else:
  print(False)'''
#smallest element
'''arr=[0,-10,1,3,-20]
# arr=[1,2,3,4,5]
for i in range(1,len(arr)+2):
  if i not in arr:
    print(i)
    break''' 
#To Find max element with size 3
'''arr = [1,2,3,1,4,5,2,3,6]
# arr=[1,2,3]
subarray=[]
k=3
for i in range(len(arr)):
  for j in range(i,len(arr)):
    subarray.append(arr[i:j+1])
for r in subarray:
  if len(r)==k:
    print(max(r))'''
arr=[335,501,170,725,479,359,963,465,706,146,282,828,962,492,996,943,828,437,392,605,903,154,293,383,422,717,719,896,448,727,772,539,870,913,668,300,36,895,704,812,323,334]
# arr=[1,4,45,6,10,8]
# arr=[1,2,4,3,6]
# x=468

'''com=set()
for i in range(len(arr)):
  if x-i in com:
    print(True)
  com.add(arr[i])
print(com)'''

'''count=0
Result=[]
while len(arr)!=count:
  for i in range(len(arr)):
    if arr[count]+arr[i]==x and arr[i]!=arr[count]:
      Result.append(arr[i])
      break
  count=count+1
print(Result)'''

'''result=[]
for i in range(len(arr)):
  for j in arr[i:]:
    if arr[i]!=j and arr[i]+j==x:
      result.append(arr[i])
if result:
  print("Yes")
else:
  print("No")'''

'''arr = [0,0,2,1,1,1]
if 1 in arr:
  Result_one = arr.index(1)
  print(Result_one)
else:
  print(-1)'''

a=[2,3,2,3,5]
Result=a[::]
n=4
count_one=0
count_Two=0
'''for i in range(1,n+1):
  if i not in Result:
    a[i-1]=0
  else:
    count=Result.count(i)
    a[i-1]=count
print(a)'''

'''for i in range(1,n+1):
  count=Result.count(i)
  a[i-1]=count
print(a)'''


'''while count_one != len(a):
  count=Result.count(count_one+1)
  a[count_one]=count
  count_one=count_one+1
print(a)'''

# arr=[(0,0,1,1),(0,0,1,1),(1,1,1,1),(0,1,0,1)]
# arr = [(0,0),(0,0)]
'''arr =[(0,0,0),(1,1,1),(1 ,1 ,1) ,(0 ,0 ,0),(0 ,1 ,1),(1,1,1) ,(0 ,0 ,0),(0 ,1 ,1),(1,1,1)]
Max = -1
count = 0
for i in range(len(arr)):
  Sum = sum(arr[i])
  if Sum>count:
    count = Sum
    Max=i
print(Max)'''
# arr=["geeksforgeeks","geeks","geek","geezer"]
'''arr=["d","d","d","d"]
arr=["akanksha","akaksha" ,"akaaka" ,"akadaka"]
arr=["aofsvugkrphjhxbnkekbcfodrdvdgrzjihd","bloscxejwhyglijpnxshcpmljluruzwvkmqmjwxhdvnoezgtyyabommzaisuhostdkfogewjbl", "fkdbjebmuqytqilmpbeieopvuvrdwcdcpifyogmkwmdouqblsh"]
str=""
for i in zip(*arr):
  Result = i[0]
  count=0
  for j in i:
    if Result==j:
      count=count+1
      if count==len(i):
        str+=Result
print(str)'''

# arr=[[1,2,3,4],
#      [5,6,7,8],
#      [9,10,11,12],]
    #  [13,14,15,16]]
arr=[[22,20,29,17],
     [6,21 ,13,19],
     [17 ,11 ,3 ,5],
     [29 ,27 ,16 ,21] ,
     [10 ,11 ,21 ,7]]
s=[]
s.extend(arr[0])

# 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
# 1 2 3 4 8 12 11 10 9 5 6 7
# 22 20 29 17 19 5 21 7 21 11 10 29 17 6 21 13 3 16 27 11
'''for i in range(1,len(arr)):
  s.append(arr[i][-1])
s.extend(arr[-1][:-1][::-1])
sec = []
se = []
for j in arr[1:-1]:
  sec.append(j[0])
  print(j[1:-1])
s.extend(sec[::-1])
s.extend(se)
print(s)'''



# arr  = [10,20,30,40,50,60,70,80,90,100,110]
'''arr=[1,2,3,4,5,6]
6, 1,5,2,4,3
Reverse = arr[::-1]
count=0
for i in range(0,len(Reverse),2):
  arr.insert(i,Reverse[count])
  arr.pop()
  count=count+1
print(arr)'''
 


# arr = [2,2,2,2,2]
'''arr = [1,2,2,4]
Copy = arr[::]
for i in range(len(Copy)):
  count=arr.count(Copy[i])
  if count>1:
    arr.remove(Copy[i])
print(arr)'''

Number = int(input("Enter Number"))

if Number>10 or Number<1:
  print(True)
else:
  print(False)




 










  