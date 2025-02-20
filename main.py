from model import llm, params, _inference
from customer_service import CustomerService
from map_customer_service import mapping, functions

import json

from mtkresearch.llm.prompt import MRPromptV2

prompt_engine = MRPromptV2()

# stage 1: query
conversations = [
    {"role": "system", "content": "You are a customer service staff of school club. Member will ask you about club information or announcements."},
]
print("AI: Hello, I am AI club customer. How can I help you?")
      
while True:
    user_input = input("you (輸入 'exit' 結束): ")
    if user_input.lower() == 'exit':
        print("程式結束。")
        break

    conversations.append({"role": "user", "content": str(user_input)})
    
    prompt = prompt_engine.get_prompt(conversations, functions=functions)
    
    output_str = _inference(prompt, llm, params)
    result = prompt_engine.parse_generated_str(output_str)

    if 'content' in result:
        print("AI 回答:", result['content'])
    
    
    # stage 2: execute called functions
    conversations.append(result)
    
    if 'tool_calls' in result and result['tool_calls']:
        tool_call = result['tool_calls'][0]
        func_name = tool_call['function']['name']
        func = mapping[func_name]
        arguments = json.loads(tool_call['function']['arguments'])
        called_result = func(**arguments) # 得到上面自訂function return的資料
    
        # print("\n\n********************** caleed_result = ",called_result, "\n")
    
    # stage 3: put executed results
        conversations.append(
            {
                'role': 'tool',
                'tool_call_id': tool_call['id'],
                'name': func_name,
                'content': json.dumps(called_result)
            }
        )
    
        prompt = prompt_engine.get_prompt(conversations, functions=functions)
    
        output_str2 = _inference(prompt, llm, params)
        result2 = prompt_engine.parse_generated_str(output_str2)
        # print(result2)
        print("AI 回答:", result2['content'])

# do you know what course be held in 2024-09-12 ?

# do you know the course topic between last year?
# how about today
# where is the course be held
# when is today's course be held?
# do u know which day is the final presentation