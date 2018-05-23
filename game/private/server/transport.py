import sys
import json

def request():
    request = sys.stdin.read()
    
    return json.loads(request)

def reply(resp):
    print(json.dumps(resp), flush=True)
    sys.exit(0)
