import cohere
import json

#importing JSON files
with open('/home/cherry/Programs/Arch App/json/meta_schema.json', 'r') as file:
    schema = json.load(file)

with open('/home/cherry/Programs/Arch App/json/object_count.json', 'r') as file:
    obj_count = json.load(file)

def update_count():
    with open('/home/cherry/Programs/Arch App/json/object_count.json', 'w') as file:
        json.dump(obj_count, file)

def reset_count():
    with open('/home/cherry/Programs/Arch App/json/object_count.json', 'w') as file:
        o = {"Rectangle": 0, "Circle": 0, "Triangle": 0}
        json.dump(o, file)
        obj_count = o


#AI configuration
co = cohere.ClientV2(api_key="o7FeLzmHrp6F3CtZ0bxHd9VnUWixwm58jLCTTUVd")
system_message = '''
create the json using the json schema based on the user's message.
Only fill out the required properties.
'''

def JSONGeneration(prompt):

    res = co.chat(
        model="command-r-plus-08-2024",
        messages=[
            {
                "role" : "system",
                "content" : system_message,
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        response_format={"type" : "json_object", "schema" : schema}
    )
    
    a = res.message.content[0].text
    res_dict = json.loads(a)
    shape_name = (res_dict['shape'])

    #Generating ID for shapes.
    #i hate python for not having switch case
    if(shape_name == 'Rectangle'):
        obj_count['Rectangle'] += 1
    elif (shape_name == 'Circle'):
        obj_count['Circle'] += 1
    elif (shape_name == 'Triangle'):
        obj_count['Triangle'] += 1

    update_count()
    res_dict['id'] = shape_name + str(obj_count[shape_name])
    
    print(res_dict)

JSONGeneration("draw a triangle")