import jwt
import json

with open('secret.json') as json_file:
    secret = json.load(json_file)['secret']

dataJson = {
    'hello': 'weird'
}

encoded = jwt.encode(dataJson, secret, algorithm='HS256')

print(encoded)

encoded_test = encoded

decoded = jwt.decode(encoded_test, secret, algorithms=['HS256'])

# print(decoded)

