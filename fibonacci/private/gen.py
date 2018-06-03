from random import randint as rnd, seed

seed(0x31337 + 0x7 * 0x1337)
task = open("../public/task.txt", "w")

# returns (gcd(a, b), x, y) such that ax+by=1
def gcdex(a, b):
    if b == 0:
        return (a, 1, 0)
    d, x1, y1 = gcdex(b, a % b)
    return (d, y1, x1 - (a // b) * y1)

# get integers (x,y) such that ax+by=n, x>=0, y>=0(?)
def solve(a, b, n):
    _, x, y = gcdex(a, b)
    x *= n
    y *= n
    
    while x > 0:
        x -= b
        y += a
    
    while x < 0:
        x += b
        y -= a
    
    return (x, y)

def get_longest(x):
    a = 1
    b = 1
    n = 3
    while a + b < x:
        a, b = b, a + b
        n += 1
    
    for _ in range(rnd(0, 12)):
        a, b = b - a, a
        n -= 1
    
    return (n, *solve(a, b, x))
    

FLAG = "ugra_f1b0nacci_sa1ad_1sn't_ta5ty_bu7_v3ry_hug3_t0_ca1cu1at3!"

def gen(let):
    num = ord(let) * 1000 + rnd(0, 999)
    
    n, a1, a2 = get_longest(num)
    
    print("F(1) = {:>6d}, F(2) = {:>6d}, F({}) = ?".format(a1, a2, n), file=task)
    
for char in FLAG:
    gen(char)

print(file=task)
print("And then find quotient of division each number by 1000", file=task)
    
task.close()