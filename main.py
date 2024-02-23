import os
import json
from fastapi import FastAPI
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import uvicorn
from llm import prepara_llm
from prompt import TABELA_COMANDOS_STR, prepara_prompt

app = FastAPI()

def test():
  prompt = prepara_prompt()
  llm = prepara_llm(prompt)
  while True:
      print("\n")
      texto_usuario = input("Digite o comando desejado: ")
      #result = obtem_comando.run(texto=texto_usuario, tabela=TABELA_COMANDOS_STR)
      result = llm.invoke({"texto": texto_usuario, "tabela": TABELA_COMANDOS_STR})
      print("Comando:"+result["text"])


class UsuarioInput(BaseModel):
    texto_usuario: str

@app.post("/obtem_comando_menu/")
def obtem_comando_menu(usuario_input: UsuarioInput) -> str:
  prompt = prepara_prompt()
  llm = prepara_llm(prompt)
  result = llm.invoke({"texto": usuario_input, "tabela": TABELA_COMANDOS_STR})
  print("Comando:"+result["text"])
  return result["text"]

  
if __name__ == "__main__":
  #test()
  uvicorn.run("main:app", host="0.0.0.0", port=8106)


# para testar
# curl -X "POST" "http://localhost:8106/obtem_comando_menu/" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"texto_usuario\": \"novo produto\"}"

