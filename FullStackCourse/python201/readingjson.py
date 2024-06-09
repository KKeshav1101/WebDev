import json
c3p0="{'name':'c-3P0'}" #sample json 
c3p0 = json.loads(c3p0)
#c3p0= json.dumps()
print(c3p0['name'])
