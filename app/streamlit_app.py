import streamlit as st
from langchain import hub
from langchain.tools import Tool
from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.llms import OpenLLM
from langchain_community.callbacks.streamlit import (
    StreamlitCallbackHandler,
)

from prompt import template
from length_tool import get_word_length

st_callback = StreamlitCallbackHandler(st.container())
llm = OpenLLM(server_url='http://openllm:3000', server_type='http')
tools = [
    Tool.from_function(
        name="Length Calculator",
        description="To calculate the length of input",
        func=get_word_length
    ),
    Tool.from_function(
        name="General Chat",
        description="For general chat not covered by other tools",
        func=llm.invoke,
    )
]
prompt = hub.pull("hwchase17/react")
#prompt = template
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)

if prompt := st.chat_input():
    st.chat_message("user").write(prompt)
    with st.chat_message("assistant"):
        st_callback = StreamlitCallbackHandler(st.container())
        response = agent_executor.invoke(
            {"input": prompt}, {"callbacks": [st_callback]}
        )
        st.write(response["output"])