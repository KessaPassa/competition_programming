# n = int(input())
# a_list = input()

# before_list = a_list
# for y in range(1, n):
#     next_list = ''
#     for x in range(len(before_list)-1):
#         next_value = abs(int(before_list[x]) - int(before_list[x+1]))
#         next_list += str(next_value)

#     before_list = next_list
#     next_list = ''

# print(before_list[0])

n = int(input())
a_list = input()

before_list = [a_list[:-1], a_list[1:]]
for y in range(1, n):
    next_list = ''
    for a, b in zip(before_list[0], before_list[1]):
        next_list += str(abs(int(a)-int(b)))

    before_list[0] = next_list[:-1] if len(next_list) > 1 else next_list[0]
    before_list[1] = next_list[1:] if len(next_list) > 1 else next_list[0]
    next_list = ''

print(before_list[0])
