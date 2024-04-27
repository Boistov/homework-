my_list = input().split()
n = int(input())

list_two = ()
for i in range(1, n+1):
    for item in my_list:
        list_two += (f"{item}{i}",)

print(list_two)

