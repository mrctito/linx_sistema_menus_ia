import os
import json
from langchain_openai import AzureChatOpenAI, ChatOpenAI
from langchain.prompts import PromptTemplate, BasePromptTemplate
from langchain.chains import LLMChain


def cria_llm_openai(verbose: bool = False):
    llm = ChatOpenAI(temperature=0, verbose=verbose, model=os.getenv("MODEL_NAME"))
    return llm


def cria_llm_azure(verbose: bool = False):
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
        verbose=verbose
    ) 
    return llm


def cria_llm(verbose: bool = False):
    if os.getenv("USE_AZURE", "N") == "S":
        llm = cria_llm_azure(verbose=verbose)
    else:
        llm = cria_llm_openai(verbose=verbose)
    return llm


def cria_chain(prompt: PromptTemplate, verbose: bool = False, llm = None):
    if llm is None:
        llm = cria_llm()
    chain = LLMChain(llm=llm, prompt=prompt, verbose=verbose)
    return chain
