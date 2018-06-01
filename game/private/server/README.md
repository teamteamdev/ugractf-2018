# Server API documentation

## Common format

Send TCP-request to `gameserver.ugractf.ru:31337` with JSON-object in body. EOF marker is `\n` newline character. Avoid it in your object.

JSON-object should contain one **required** field `method` and fields for arguments (see respective method description).

Response contains one JSON-object with **required** field `status` and fields with result (see respective method description).

If request is not well-formed, returned value will contain only one field `status: "bad"`.

If method does not exist, returned value will contain only one field `status: "no-method"`.

## users.register

Registers a user. Initial score is 0, initial time is 0m0s.

### Arguments

* `method: "users.register"`
* `nickname` — string, required

### Returns

* `status: "ok"` if succeeded
* `status: "found"` if username exists
* `status: "denied"` if username is denied by server policy

### Example

```javascript
> {"method": "user.register", "nickname": "batya"}
< {"status": "ok"}
```

## users.record

Records new highscore. If it is worse than previous, highscore does not update

### Arguments

* `method: "users.record"`
* `nickname` — string, required
* `score` — int, required, should be non-negative
* `time` — int, required, in seconds
* `checksum` — string, required — SHA-256 hash of string (`nickname + str(score) + str(time) + "se4v7qahjtp3bywrug86x"`)

### Returns

* `status: "ok"` if succeeded
* `status: "skipped"` if current score is better
* `status: "denied"` if hashsum is not correct
* `status: "unknown"` if user is not registered

### Example

```javascript
> {"method": "users.record", "nickname": "batya", "score": 222, "time": 1337, "checksum": "7d3fe07de0603913ad37debf51635db87faa07033591e56a9175776e12b35109"}
< {"status": "skipped"}
```

## users.scoreboard

Returns the scoreboard. Server **guarantees** that it is sorted by score in descreasing order, then by time in increasing order.

### Arguments

* `method: "users.scoreboard"`

### Returns

* `status: "ok"`
* `users` — list of objects with fields:
   * `nickname` — string
   * `score` — highscore
   * `time` — time associated with this score
   
### Example

```javascript
> {"method": "users.scoreboard"}
< {"status": "ok", "users": [{"nickname": "batya", "score": 489, "time": 228}]}
```

## billing.buy

Processes flag purchases. **Now we accept only Vika payment system**. Visa, MIR and Mastercard are to be implemented in 2019.

### Arguments

* `method: "billing.buy"`
* `card` — object with fields:
   * `number` — string, 13 to 19 digit card number
   * `holder` — string, cardholder name
   * `expires` — string, in format `mm/yy`, `int(mm) < 12`, at least `06/18`
   * `cvc` — string, 3 to 4 digit secure code

### Returns

* `status: "ok"` if payment is succeeded
   * in this case field `messages` is also present. It is array of Message objects:
     * `nickname` — string, user name
     * `timestamp` — integer, message timestamp
     * `message` — message contents itself
* `status: "invalid"` if card is invalid
* `status: "denied"` if bank has denied the payment
* `status: "unsupported"` if payment system is not supported now

### Example

```javascript
> {"method": "billing.buy", "card": {"number": "7012340013376661", "holder": "PETER PWNER", "expires": "02/28", "cvc": "555"}}
< {"status": "ok", "code": "ugra_flag3_sup3r_d3bug_m0d3_3nab13d"}
```

### Note

The only existing card in Vika payment system for current moment is listed in “Example” section.

## billing.checkPromo

Processes promo code redeeming.

### Arguments

* `method: billing.checkPromo`
* `code` — string, required, promocode value

### Returns

* `status: ok` if code is redeemed
* `status: limited` if user has reached activation limit
* `status: invalid` if code does not exist

### Note

* Promo codes from UPML CTF 2017 Summer (`CTF-...`) have activation limit: **5 tries per promocode**
* Promo code `TEST-A6Y327D` is for debugging purposes and does not have activation limit