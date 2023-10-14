with open('json_test.txt','r') as f:
    s=f.read()

print(s)


import json
book =json.loads(s)

print(book)

print(book['tom'])