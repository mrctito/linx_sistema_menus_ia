from fastapi import FastAPI
from pydantic import BaseModel
from llm import prepara_llm
from prompt import TABELA_COMANDOS_STR, prepara_prompt

app = FastAPI()

class UsuarioInput(BaseModel):
    texto_usuario: str

@app.post("/obtem_comando_menu/")
def obtem_comando_menu(usuario_input: UsuarioInput) -> dict:
  prompt = prepara_prompt()
  llm = prepara_llm(prompt)
  result = llm.invoke({"texto": usuario_input, "tabela": TABELA_COMANDOS_STR})
  print("Comando:"+result["text"])
  return result["text"]
