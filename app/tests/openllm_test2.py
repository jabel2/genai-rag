from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from llm import llm

template = "What is a good name for a company that makes keyboards and coffee?"

prompt = PromptTemplate.from_template(template)

llm_chain = LLMChain(prompt=prompt, llm=llm)

#generated = llm_chain.invoke(product="mechanical keyboard")
generated = llm_chain.invoke({"input": prompt})
print(generated)