#!/usr/bin/env python3

from models import *

print("\033[1;33mGameserver Dumper\033[0m\n")

print("[U]sers, [C]oupons or [M]essages? ", end="")

data = input().lower().strip()

db.connect()

print()

if data[0] == "u":
    print("{:<30s} | {:<10s} | {}".format("User", "Score", "Time"))
    print("-"*31 + "|" + "-"*12 + "|" + "-"*11)
    for user in User.select().order_by(User.score.desc(), User.time):
        print("{:<30s} | {:<10d} | {}".format(user.nickname, user.score, user.time))
    print("-"*31 + "|" + "-"*12 + "|" + "-"*11)
elif data[0] == "c":
    print("{:<30s} | {:<10s} | {}".format("Code", "Usages", "Limit"))
    print("-"*31 + "|" + "-"*12 + "|" + "-"*11)
    for coupon in Coupon.select():
        print("{:<30s} | {:<10d} | {}".format(coupon.code, coupon.usages, coupon.limit))
    print("-"*31 + "|" + "-"*12 + "|" + "-"*11)
elif data[0] == "m":
    from datetime import datetime
    
    print("{:<30s} | {:<10s} | {}".format("Nickname", "Time", "Length"))
    print("-"*31 + "|" + "-"*12 + "|" + "-"*11)
    for message in Message.select():
        print("{:<30s} | {:<10s} | {}".format(message.nickname, str(message.timestamp.time()), len(message.message)))
    print("-"*31 + "|" + "-"*12 + "|" + "-"*11)
else:
    print("\033[0;31mInvalid command, exiting\033[0m")