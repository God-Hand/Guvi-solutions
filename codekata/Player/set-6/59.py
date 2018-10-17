n = int(input())
l = list(map(int,input().split()))
temp_list = []
main_list = []
for i in l:
    if i:
        temp_list.append(i)
    else:
        main_list+=temp_list
        temp_list = []

print(*main_list)
