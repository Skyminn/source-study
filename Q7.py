#예제7-1
def search_list(a,x):
    n = len(a)
    for i in range(0,n):
        if a[i]==x:
            return i
    return -1

v=[17,92,18,33,58,7,33,42]
print(search_list(v,18))
print(search_list(v,33))
print(search_list(v,900))

#연습문제 7-1
def search_list2(a,x):
    n = len(a)
    result = []
    for i in range(0,n):
        if a[i]==x:
            result.append(i)
    return result
v=[17,92,18,33,58,7,33,42]
print(search_list2(v,33))
print(search_list2(v,900))

#연습문제 7-2
#0(n)

#연습문제 7-3
def search_name(stu_no , stu_name , find_num):
    n=len(stu_no)
    for i in range(0,n):
        if find_num==stu_no[i]:
            return stu_name[i]
    return "?"
stu_no = [39, 14, 67, 105]
stu_name = ["Justin", "John", "Mike", "Summer"]
print(search_name(stu_no , stu_name ,39))
print(search_name(stu_no , stu_name ,14))
print(search_name(stu_no , stu_name ,16))