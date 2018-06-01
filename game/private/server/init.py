from models import *
import traceback, csv
from datetime import datetime

try:
    print("Task initializer working..", flush=True)

    db.connect()
    db.create_tables([User, Coupon, Message])

    print("[+] Migrations succeeded", flush=True)
    
    with open("users.csv", "r") as data:
        reader = csv.DictReader(data, delimiter=';', quotechar='"')
        
        for row in reader:
            User.create(**row)

    print("[+] Users added [flag #3 stored]", flush=True)

    coupons = open("coupons.csv")
    
    with open("coupons.csv", "r") as data:
        reader = csv.DictReader(data, delimiter=';', quotechar='"')
        
        for row in reader:
            Coupon.create(**row)
    
    print("[+] Coupons added", flush=True)
    
    with open("messages.csv", "r") as data:
        reader = csv.DictReader(data, delimiter=';', quotechar='"')
        
        for row in reader:
            h, m = map(int, row["timestamp"].split(":"))
            row["timestamp"] = datetime(2018, 6, 5, h, m).timestamp()
            Message.create(**row)
    print("[+] Messages added", flush=True)
    
    print("[*] Database is created successfully", flush=True)
    
except:
    print("[!] Something went wrong.\n    Please fix the bug and retry.\n    Debug information:", flush=True)
    traceback.print_exc()
