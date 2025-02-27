thisdict={
    "brand":"ford",
    "model":"huyandi",
    "year":1964
}
print(thisdict.get("brand"))
print(thisdict["model"])
print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())
print(thisdict.update({"cast":"vau","xomi":234}))
print(thisdict.popitem())


#list inside dictionary:
thisdict1={
    "brand":"merocar",
    "electric":False,
    "year":2233,
    "colors":['red','orange','gray']
}
print(thisdict1.items())
print(type(thisdict1))
print(dict(sorted(thisdict1.items())))
print(thisdict1.update({"color":"white"}))
thisdict1['choice']="no"
print(thisdict1)
thisdict1["year"]=22222
print(thisdict1)
if "brand" in thisdict1:
    print("yes brand exist")

print(thisdict1.popitem())
print(thisdict1.pop("brand"))
print(thisdict1.values())
print(thisdict1.keys())
for x in thisdict1:
    print(thisdict1[x])
    print(x)

cp=thisdict1.copy()
print(f"Iam copy:{cp}")

dic=dict(cp)
print(f"Hello:{dic}")


#nested dictionary
my_child={
    "child1":{
        "name":"honjau",
        "year":2024
        },
    "child2":{
        "name":"fanjau",
        "year":2000
    },
    "child3":{
        "name":"banjau",
        "year":1004
    }
}
print(my_child)

