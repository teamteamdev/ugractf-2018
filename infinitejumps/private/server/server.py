#!/usr/bin/env python3

import transport
import users, billing
import os, sys

METHODS = {
    "users.register": users.register,
    "users.record": users.record,
    "users.scoreboard": users.scoreboard,
    
    "billing.buy": billing.buy,
    "billing.checkPromo": billing.checkPromo
}

DEFAULT_METHOD = lambda **kwargs: {"status": "no-method"}

try:
    req = transport.request()
    
    transport.reply(METHODS.get(req.get("method", ""), DEFAULT_METHOD)(**req))
except (SystemExit, EOFError):
    sys.exit(0)
except Exception as e:
    transport.reply({"status": "bad"})
