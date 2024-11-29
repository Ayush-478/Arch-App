import cohere
co = cohere.ClientV2(api_key="o7FeLzmHrp6F3CtZ0bxHd9VnUWixwm58jLCTTUVd")

system_message_template = '''
You are a lighthearted chatbot.
Keep the response lighthearted, jolly and concise.'''

def Conversation(prompt, sys = None):
    
    if sys == None:
        sys = system_message_template

    res = co.chat(
        model="command-r-plus-08-2024",
        messages=[
            {
                "role" : "system",
                "content" : sys,
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
    )

    return res.message.content[0].text


