arr=[0,2,1,0,3,5,6,4]
ascending_order=[0]
for i in range(len(arr)):
  for j in range(len(ascending_order)):
    if arr[i]>=ascending_order[j]:
      ascending_order.insert(j,arr[i])
      break
ascending_order.remove(ascending_order[-1])
print(ascending_order[::-1])
