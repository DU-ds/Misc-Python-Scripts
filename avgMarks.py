n = int(input())
s = {}
for i in range(n):
    line = input()
    line = line.split()
    name = line[0]
    line.pop(0)
    s[name] = line 

# https://stackoverflow.com/questions/4426663/how-to-remove-the-first-item-from-a-list#4426727

name = input()
scores = s[name]
sum = 0
for score in scores:
    sum += float(score)

mean = sum / len(scores)
print('{:.2f}'.format(round(mean, 2)))
# https://stackoverflow.com/questions/19986662/rounding-a-number-in-python-but-keeping-ending-zeros#19986686

