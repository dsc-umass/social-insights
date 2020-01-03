import jwt
import json

with open('secret.json') as json_file:
    secret = json.load(json_file)['secret']

dataJson = "where are the pit stop locations in SF"
encoded = jwt.encode(dataJson, secret, algorithm='HS256')

print(encoded)

encoded_test = encoded

secret_test = "hello"
decoded = jwt.decode(encoded_test, secret, algorithms=['HS256'])

print(decoded)

