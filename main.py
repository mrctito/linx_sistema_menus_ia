import os
import json
from fastapi import FastAPI
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import uvicorn
from llm import cria_chain, cria_llm
from prompt import TABELA_COMANDOS_EMPORIO_STR, prepara_prompt

app = FastAPI()

# rotina para testar o serviço


def teste():
    prompt = prepara_prompt()
    llm = cria_chain(prompt)
    while True:
        print("\n")
        texto_usuario = input("Digite o comando desejado: ")
        if texto_usuario == ".":
            break

        usuario_input = UsuarioInput(
            codigo_sistema="EMPORIO", texto_usuario=texto_usuario)
        result = obtem_comando_menu(usuario_input)
        print(result)


class UsuarioInput(BaseModel):
    codigo_sistema: str
    texto_usuario: str

# serviço que recebe um comando do usuário e retorna o código de menu correspondente


def obtem_comando_menu(usuario_input: UsuarioInput) -> str:
    prompt = prepara_prompt()

    chain = cria_chain(prompt, verbose=True)

    # decide qual tabela de comandos usar
    tabela = ""
    if usuario_input.codigo_sistema == "EMPORIO":
        tabela = TABELA_COMANDOS_EMPORIO_STR
    else:
        return "0"

    result = chain.invoke({"texto": usuario_input, "tabela": tabela})
    return result["text"]


if __name__ == "__main__":
    teste()


"""
1- No programa principal, criar um campo de texto para o usuário digitar o comando desejado.
2- Chamar a API que traduz o comando do usuario em um código de menu.
3- Escrever um "case" ou "ifs aninhados" para cada código de menu, que chama a função do sistema correspondente.
"""
