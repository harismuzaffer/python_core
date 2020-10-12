n = int(input())
n*= 2
s = input().split(' ')
arr = []
count= 0
for i in range(0, n):
    arr.append(int((s[i])))

def merge_sort(arr, l, r):
    if l < r:
        m = int((l+(r-1))/2)
        merge_sort(arr, l, m)
        merge_sort(arr, m+1, r)
        merge(arr, l, m, r)

def merge(arr, l, m, r):
    n1= m- l+ 1
    n2= r- m
    arr1 = []
    arr2 = []
    for i in range(0, n1):
        arr1.append(arr[l+ i])
    for j in range(0, n2):
        arr2.append(arr[m+ 1+ j])

    i= 0
    j= 0
    k= l
    while i< n1 and j< n2:
        if arr1[i]<= arr2[j]:
            arr[k]= arr1[i]
            i+= 1
        else:
            arr[k]= arr2[j]
            j+= 1
        k+= 1

    while i< n1:
        arr[k]= arr1[i]
        i+= 1
        k+= 1
    while j< n2:
        arr[k]= arr2[j]
        j+= 1
        k+= 1

merge_sort(arr, 0, n- 1)
cc= 0
for i in range(int(n/2)):
    count += min(arr[cc], arr[cc+1])
    cc+= 2
print(count)
