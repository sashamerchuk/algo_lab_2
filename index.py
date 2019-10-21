from random import random
N=20
array=[]

for i in range(N):
   array.append(int(random()*100))
array.sort()
b = int(input())
print (array)




def binary_search(arr,left,right,item):
    middle=(left+right)//2
    if right<left:
        return middle
    if arr[middle]>item:
        return binary_search(arr,left,middle-1,item)
    elif arr[middle]<item:
        return binary_search(arr,middle+1,right,item)
    else:
        return middle

def loveStory(arr,item):
    first_index=binary_search(arr,0,len(arr)-1,item-1)
    if first_index==-1:
        return False
    first_el=0
    second_el=0
    third_el=0
    second_index=0
    third_index=0
    while first_index>=2:
        first_el=arr[first_index]
        second_el = item-first_el-1
        second_index=binary_search(arr,0,first_index-1,second_el)
        second_el=arr[second_index]
        third_el=item-first_el-second_el
        third_index=binary_search(arr,0,second_index-1,third_el)
        third_el=arr[third_index]
        if (first_el+second_el+third_el)==item:
            print("First =",first_el,"Second = ",second_el,"Third = ",third_el)
            return True
        first_index-=1
    return False

if loveStory(array,b) == True:
    print("Yes")
else:
    print("No")