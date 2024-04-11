# import streamlit as st
# from langchain_community.llms import LlamaCpp
# from langchain_community.embeddings import LlamaCppEmbeddings
# from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler

# # Callbacks support token-wise streaming
# callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

# # Make sure the model path is correct for your system!
# llm = LlamaCpp(
#     model_path="/models/mistral-7b-openorca.gguf2.Q4_0.gguf",
#     n_gpu_layers=1,
#     n_batch=512,
#     n_ctx=2048,
#     f16_kv=True,
#     temperature=0.75,
#     max_tokens=2000,
#     top_p=1,
#     callback_manager=callback_manager,
#     verbose=True,  # Verbose is required to pass to the callback manager
# )

# embeddings = LlamaCppEmbeddings(model_path="/models/mistral-7b-openorca.gguf2.Q4_0.gguf")

from langchain_community.llms import OpenLLM

llm = OpenLLM(server_url='http://openllm:3000', server_type='http')