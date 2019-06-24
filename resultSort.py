def customsort(arr) :
    return arr[1],arr[0],arr[2]

testcase=int(input("Eneter the number of test case: "))
while(testcase>0):
    size_of_student =int(input("Enter total number of student: "))
    name=input().split()
    marks=input().split()
    id=input().split()
    arr=list()
    for i in range(0,size_of_student):
        arr.append((name[i],marks[i],id[i]))
        arr.sort(key= customsort)
    for i in arr:
        print(i[1],i[0],i[2],end=" ")
    print()
    testcase-=1


