book={}

book['tom'] ={
    'name':'Tom',
    'address':'Nepal'
}

book['bob']={
    'name':'Bob',
    'address':'India'
}

import json
s=json.dumps(book)

with open('json_test.txt','w') as f:
    f.write(s)