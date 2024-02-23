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
      if texto_usuario == ".":
        break
      usuario_input = UsuarioInput(texto_usuario=texto_usuario)
      result = obtem_comando_menu(usuario_input)
      print(result)


class UsuarioInput(BaseModel):
  texto_usuario: str

@app.post("/obtem_comando_menu/")
def obtem_comando_menu(usuario_input: UsuarioInput) -> str:
  prompt = prepara_prompt()
  llm = prepara_llm(prompt)
  result = llm.invoke({"texto": usuario_input, "tabela": TABELA_COMANDOS_STR})
  return result["text"]

  
if __name__ == "__main__":
  modo_teste = os.getenv("MODO_TESTE", "N")
  if modo_teste == "S":
    test()
  else:
    print()
    print("Iniciando servidor...")
    print()
    print("Acesse http://localhost:8106/docs para Swagger")
    print()
    print("Para testar, use o comando abaixo")
    print('curl -X "POST" "http://localhost:8106/obtem_comando_menu/" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"texto_usuario\": \"novo produto\"}"')
    print()
    uvicorn.run("main:app", host="0.0.0.0", port=8106)

# para testar
# curl -X "POST" "http://localhost:8106/obtem_comando_menu/" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"texto_usuario\": \"novo produto\"}"

