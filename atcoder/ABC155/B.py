n = int(input())
a_list = list(map(int, input().split()))
can_path = True

for a in a_list:
    if a % 2 == 0:
        if not(a % 3 == 0 or a % 5 == 0):
            can_path = False

if can_path:
    print('APPROVED')
else:
    print('DENIED')
