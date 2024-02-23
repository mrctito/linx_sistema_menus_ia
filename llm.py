import os
import json
from langchain_openai import AzureChatOpenAI, ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


def prepara_llm(prompt):
    llm = ChatOpenAI(temperature=0, verbose=True)
    chain = LLMChain(llm=llm, prompt=prompt, verbose=False)
    return chain


def prepara_llm_azure(prompt):
    AZURE_DEPLOYMENT_NAME = os.getenv("AZURE_DEPLOYMENT_NAME")
    AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")
    AZURE_OPENAI_API_BASE = os.getenv("AZURE_OPENAI_API_BASE")
    AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
    AZURE_OPENAI_API_TYPE, = os.getenv("AZURE_OPENAI_API_TYPE")

    llm = AzureChatOpenAI(
        deployment_name=AZURE_DEPLOYMENT_NAME,
        openai_api_version=AZURE_OPENAI_API_VERSION,
        openai_api_base=AZURE_OPENAI_API_BASE,
        openai_api_key=AZURE_OPENAI_API_KEY,
        openai_api_type=AZURE_OPENAI_API_TYPE,
        temperature=0,
        verbose=True
    ) 

    chain = LLMChain(llm=llm, prompt=prompt, verbose=False)
    return chain
