import transport
import users, billing

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
except SystemExit:
    raise
except:
    transport.reply({"status": "bad"})
