from langchain_community.llms import OpenLLM

llm = OpenLLM(server_url='http://openllm:3000', server_type='http')
result = llm.invoke('What is the difference between a duck and a goose? And why there are so many Goose in Canada?')
print(result)