import sys, json, logger

def request():
    request = input()
    logger.log(request)
    return json.loads(request)

def reply(resp):
    print(json.dumps(resp), flush=True)
    logger.log(json.dumps(resp), out=True)
    sys.exit(0)
