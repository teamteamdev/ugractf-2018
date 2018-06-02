from models import *
import hashlib

def register(method, nickname):
    db.connect()
    
    if "ugra" in nickname.lower():
        return {"status": "denied"}
    if "flag" in nickname.lower():
        return {"status": "denied"}
    
    try:
        user = User.get(User.nickname == nickname)
        
        return {"status": "found"}
    except User.DoesNotExist:
        User.create(nickname=nickname)
        
        return {"status": "ok"}

def record(method, nickname, score, time, checksum):
    db.connect()

    correct_checksum = hashlib.sha256((nickname + str(score) + str(time) + "se4v7qahjtp3bywrug86x").encode()).hexdigest()
    if checksum != correct_checksum:
        return {"status": "denied"}
    
    try:
        user = User.get(User.nickname == nickname)
    except User.DoesNotExist:
        return {"status": "unknown"}
    
    if user.score > score:
        return {"status": "skipped"}
    
    if user.score == score and user.time < time:
        return {"status": "skipped"}
        
    user.score = score
    user.time = time
    user.save()
    return {"status": "ok"}
        
def scoreboard(method):
    db.connect()
    
    users = []
    for user in User.select().order_by(User.score.desc(), User.time):
        users.append({
            "nickname": user.nickname,
            "score": user.score,
            "time": user.time
        })
    
    return {
        "status": "ok",
        "users": users
    }
