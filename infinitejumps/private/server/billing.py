from models import *

def _check(number):
    if len(number) < 13 or len(number) > 19:
        return False
    res = 0
    for i in range(len(number)):
        d = (2 - i % 2) * int(number[i])
        if d > 9:
            d -= 9
        res += d
    return res % 10 == 0

def buy(method, card):
    if not _check(card["number"]):
        return {"status": "invalid"}
    if card["number"][:6] != "701234":
        return {"status": "unsupported"}
    
    if (card["number"] == "7012340013376661" and
        card["holder"].upper().strip() == "PETER PWNER" and
        card["expires"] == "02/28" and
        str(card["cvc"]) == "555"):

        
        messages = []
        for message in Message.select().order_by(Message.timestamp):
            messages.append({
                "nickname": message.nickname,
                "timestamp": int(message.timestamp.timestamp()),
                "message": message.message
            })
    
        return {
            "status": "ok",
            "messages": messages
        }
    else:
        return {"status": "denied"}

def checkPromo(method, code):
    db.connect()
    
    try:
        coupon = Coupon.get(Coupon.code == code)
    except Coupon.DoesNotExist:
        return {"status": "invalid"}
    
    if coupon.limit != 0 and coupon.usages >= coupon.limit:
        return {"status": "limited"}
    
    coupon.usages += 1
    coupon.save()
    
    return {"status": "ok"}
