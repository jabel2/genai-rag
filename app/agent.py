from langchain.tools import Tool
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain import hub
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_core.prompts import PromptTemplate

from llm import llm
from prompt import prompt_template

# Use the Chains built in the previous lessons
#from tools.vector import kg_qa
# from solutions.tools.fewshot import cypher_qa
#from solutions.tools.finetuned import cypher_qa


tools = [
    Tool.from_function(
        name="General Chat",
        description="For general chat not covered by other tools",
        func=llm.invoke,
        # return_direct=True
    ),
    # Tool.from_function(
    #     name="Cypher QA",
    #     description="Provide information about movies questions using Cypher",
    #     func = cypher_qa,
    #     return_direct=True
    # ),
    # Tool.from_function(
    #     name="Vector Search Index",
    #     description="Provides information about movie plots using Vector Search",
    #     func = kg_qa,
    #     return_direct=True
    # )
]

memory = ConversationBufferWindowMemory(
    memory_key='chat_history',
    k=5,
    return_messages=True,
)
template = "What is a good name for a coffee cup? {prompt}"
agent_prompt = PromptTemplate.from_template(template)

agent = create_openai_tools_agent(llm, tools, agent_prompt)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    memory=memory,
    verbose=True
    )

def generate_response(prompt):
    """
    Create a handler that calls the Conversational agent
    and returns a response to be rendered in the UI
    """
    response = agent_executor.invoke({"input": prompt})
    return response