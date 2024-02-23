import os
import json
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


"""
Sugestão: Trocar por AZureOpenAI
"""
def prepara_llm(prompt):
    llm = ChatOpenAI(temperature=0, verbose=True)
    chain = LLMChain(llm=llm, prompt=prompt, verbose=False)
    return chain
