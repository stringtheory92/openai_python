import openai
from dotenv import load_dotenv
import os


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


model_id = 'gpt-4'
# model_id = 'gpt-3.5-turbo'

def ChatGPT_conversation(conversation):
    response = openai.ChatCompletion.create(
        model=model_id,
        messages=conversation
    )
    api_usage = response['usage']

    print('Total tokens consumed: {0}'.format(api_usage['total_tokens']))
    # stop means complete
    print(response['choices'][0].finish_reason)
    print(response['choices'][0].index)

    conversation.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
    return conversation
                         

# system, assistant, user

system_message = f"""your purpose is to infer and generate two datapoints (labeled material and texture_type)from a given name of an object or element of a picture. 
                The element will come from user input and could be anything. Use your best judgment to infer what type of material it's made of and what its texture must be. 
                Your response should include only one value for material, and one for texture_type. 
                It should be in JSON format like this: material: material, texture_type: texture_type
                The list of possible material values are: metal, wood, stone, cloth, rubber
                The list of possible texture_type values are: smooth, soft, sticky, rough_fine, rough_coarse
                """

conversation = []
conversation.append({'role': 'system', 'content': system_message})

c_function = ChatGPT_conversation(conversation)
print('{0}; {1}\n'.format(c_function[-1]['role'], c_function[-1]['content'].strip()))

while True: 
    prompt = input('User:')
    conversation.append({'role': 'user', 'content': prompt})
    c_function = ChatGPT_conversation(conversation)
    print('{0}: {1}\n'.format(c_function[-1]['role'].strip(), c_function[-1]['content'].strip()))