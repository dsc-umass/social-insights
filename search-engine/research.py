import jwt

secret = "hello"
encoded = jwt.encode({'some': 'payload'}, secret, algorithm='HS256')

print(encoded)

encoded_test = encoded

decoded = jwt.decode(encoded_test, secret, algorithms=['HS256'])

print(decoded)