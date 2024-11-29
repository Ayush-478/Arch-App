
import cohere
co = cohere.ClientV2(api_key="o7FeLzmHrp6F3CtZ0bxHd9VnUWixwm58jLCTTUVd")

system_message_template = '''
## Task and Context

You determine if the user wants a conversation or a JSON response. 
A conversation prompt is when the user wants to talk, 
while a JSON request is when they want something done or generated. 
You only judge the prompt, not generate responses, you only respond in binary.
Just response with "0" if you think its a conversational prompt and "1", for json prompt.

##Example of a conversational promts-

1. Hey, hello!
2. How are you
3. What do you do
4. What is my/your name
5. What a day today huh?
6. Nice view
7. Good job
8. Thank you

##Example of prompts asking for a json generation

1. Add a circle
2. Add a house next to the circle
3. Paint it blue
4. Make a rectangle of length 100m.
5. change the size to 20m
6. Strecht the triangle
7. rotate the square
8. Add a cylinder
9. Draw a square to the north side of the canvas.
'''

def Doorkeeper(prompt):

    res = co.chat(
        model="command-r-plus-08-2024",
        messages=[
            {
                "role" : "system",
                "content" : system_message_template,
            },
            {
                "role": "user",
                "content": prompt,
            }
        ],
        temperature = 0.3,
    )
    return res.message.content[0].text
