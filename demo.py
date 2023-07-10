import openai
from dotenv import load_dotenv
import os


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


model_id = 'gpt-3.5-turbo'

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

conversation = []
conversation.append({'role': 'system', 'content': 'How may I help you'})

c_function = ChatGPT_conversation(conversation)
print('{0}; {1}\n'.format(c_function[-1]['role'], c_function[-1]['content'].strip()))

while True: 
    prompt = input('User:')
    conversation.append({'role': 'user', 'content': prompt})
    c_function = ChatGPT_conversation(conversation)
    print('{0}: {1}\n'.format(c_function[-1]['role'].strip(), c_function[-1]['content'].strip()))