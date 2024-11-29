import json

a= {
  "action": "delete",
  "shape": "Triangle",
  "position":{

"x": 100,
"y": 100
}

,
"dimensions": {
  "width": 100,
  "height": 100
}
,
"style": {
  "strokeColor": "black",
  "lineWidth": 1
}
}

b = json.loads(a)

print(b['position'])