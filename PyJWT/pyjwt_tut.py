# Use pyjwt to decode JSON web tokens

import jwt
import datetime
import time

payload = {
    "uid": 23,
    "name": "vish",
    "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=2)
}

SECRETKEY = "N0TV3RY53CR3T"

# encode the payload
token = jwt.encode(payload=payload, key=SECRETKEY)
print("Generated Token: {}".format(token.decode()))
print("Generated Token: {}".format(token))

# Expiry of ten seconds
time.sleep(1)

# decode the token with secret key and payload
decoded_payload = jwt.decode(jwt=token, key=SECRETKEY)

print(decoded_payload)



