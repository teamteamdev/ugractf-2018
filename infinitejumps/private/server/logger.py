from datetime import datetime
import os

LOG_PATH = "/tmp/gameserver/log.txt"

def log(data, out=False):
    ip = os.getenv("SOCAT_PEERADDR", "???.???.???.???")
    f = open(LOG_PATH, "a")
    
    if out and len(data) > 30:
        data = data[:30] + "..."
    
    print("{} - {} {} {}".format(
        str(datetime.now()), ip, "<" if out else ">", data
    ), file=f)
    f.close()
