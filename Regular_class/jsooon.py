import json

x='{"name":"sudarshan", "cast":"khatri","age":30,"city":"newyork"}'

y=json.loads(x)
print(y["age"])


z='{"name":"sudarshan", "cast":"khatri","age":30,"city":"newyork"}'

y=json.dumps(z)
print(y)