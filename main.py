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
    while True:
        print("\n")
        texto_usuario = input("Digite o comando desejado: ")
        if texto_usuario == ".":
            break

        # PRINCIPAL
        result = obtem_comando_menu(texto_usuario)
        print(result)


def obtem_comando_menu(usuario_input: str) -> str:
    prompt = prepara_prompt()

    chain = cria_chain(prompt, verbose=True)

    # decide qual tabela de comandos usar
    tabela = TABELA_COMANDOS_EMPORIO_STR

    result = chain.invoke({"texto": usuario_input, "tabela": tabela})
    return result["text"]


if __name__ == "__main__":
    teste()
