import re

n = int(input())
s = input()

repeater = re.compile('ABC')
result = repeater.findall(s)
print(len(result))
