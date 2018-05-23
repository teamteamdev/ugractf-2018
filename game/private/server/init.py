from models import *
import traceback

FLAG = "ugra_g0_f31ch_4_41ag"

try:
    print("Task initializer working..", flush=True)

    db.connect()
    db.create_tables([User, Coupon])

    print("[+] Migrations succeeded", flush=True)

    User.create(nickname=FLAG, score=-1337, time=666)
    
    print("[+] Flag stored", flush=True)
    
    User.create(nickname="batya", score=225, time=56)
    User.create(nickname="nagibator", score=800, time=154)
    User.create(nickname="cucumber", score=50, time=883)
    User.create(nickname="test", score=0, time=50)
    User.create(nickname="lesya2018", score=220, time=0)
    User.create(nickname="admin", score=340, time=44)
    User.create(nickname="keklolcheburek", score=615, time=158)
    User.create(nickname="player1147", score=650, time=205)
    User.create(nickname="pashman", score=740, time=1260)
    User.create(nickname="snowlabs", score=700, time=320)
    
    print("[+] Demo users created", flush=True)
    
    coupons = open("coupons.txt")
    
    for line in coupons:
        code, limit = line.split()
        Coupon.create(code=code, limit=limit)
    
    print("[+] Coupons created", flush=True)
    
    print("[*] Database is created successfully", flush=True)
    
except:
    print("[!] Something went wrong.\n    Please fix the bug and retry.\n    Debug information is below:", flush=True)
    traceback.print_exc()
