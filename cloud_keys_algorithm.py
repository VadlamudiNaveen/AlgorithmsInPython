import hashlib
res = {}
while True:
    msg = input()
    hash = hashlib.sha256(msg.encode()).hexdigest()
    if hash not in res:
        res[msg] = hash
    print(res)