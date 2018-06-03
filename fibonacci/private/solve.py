import re

task = open("../public/task.txt")

for line in task:
    result = re.match(r"F\(1\) = +([-0-9]+), F\(2\) = +([-0-9]+), F\((\d+)\)", line)
    
    if result is None:
        continue
    
    a1, a2, n = map(int, result.group(1, 2, 3))
    
    for i in range(2, n):
        a1, a2 = a2, a1 + a2
        
    print(a2 // 1000, end=' ')
print()
