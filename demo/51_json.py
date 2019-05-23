import json

# json data
x = '{"name":"Json", "age":30,"city":"New York"}'

# parse json data
y = json.loads(x)

print("Age : "+str(y["age"]))


