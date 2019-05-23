import json

print(json.dumps({"name":"Jack","age":31}))
print(json.dumps(["apple","banana"]))
print(json.dumps(("apple","banana")))
print(json.dumps("hello"))
print(json.dumps(55))
print(json.dumps(24.55))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))