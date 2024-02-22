import os
import json
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from llm import prepara_llm
from prompt import TABELA_COMANDOS_STR, prepara_prompt


def test():
  prompt = prepara_prompt()
  llm = prepara_llm(prompt)
  while True:
      print("\n")
      texto_usuario = input("Digite o comando desejado: ")
      #result = obtem_comando.run(texto=texto_usuario, tabela=TABELA_COMANDOS_STR)
      result = llm.invoke({"texto": texto_usuario, "tabela": TABELA_COMANDOS_STR})
      print("Comando:"+result["text"])


def obtem_comando_menu(texto: str) -> str:
  prompt = prepara_prompt()
  llm = prepara_llm(prompt)
  result = llm.invoke({"texto": texto_usuario, "tabela": TABELA_COMANDOS_STR})
  print("Comando:"+result["text"])
  return result["text"]
   