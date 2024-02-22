import os
import json
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

TABELA_COMANDOS = [
  {
    "command": "cadastrar novo produto",
    "description": "Adicionar um novo produto ao inventário",
    "code": "CMD1000001"
  },
  {
    "command": "atualizar estoque",
    "description": "Atualizar a quantidade de um produto no estoque",
    "code": "CMD1000002"
  },
  {
    "command": "remover produto",
    "description": "Remover um produto do inventário",
    "code": "CMD1000003"
  },
  {
    "command": "verificar níveis de estoque",
    "description": "Consultar a quantidade atual de produtos no estoque",
    "code": "CMD1000004"
  },
  {
    "command": "relatório de estoque",
    "description": "Gerar um relatório detalhado do estoque",
    "code": "CMD1000005"
  },
  {
    "command": "cadastrar fornecedor",
    "description": "Adicionar um novo fornecedor ao sistema",
    "code": "CMD1000006"
  },
  {
    "command": "excluir fornecedor",
    "description": "Remover um fornecedor do sistema",
    "code": "CMD1000007"
  },
  {
    "command": "registrar entrada de produtos",
    "description": "Registrar a entrada de novos produtos no estoque",
    "code": "CMD1000008"
  },
  {
    "command": "registrar saída de produtos",
    "description": "Registrar a saída de produtos do estoque",
    "code": "CMD1000009"
  },
  {
    "command": "analisar tendências de estoque",
    "description": "Analisar padrões e tendências no movimento de estoque",
    "code": "CMD1000010"
  }
]

TABELA_COMANDOS_STR = json.dumps(TABELA_COMANDOS)

PROMPT_BASE = """
Com base na tabela de mapeamento de comandos e códigos de um sistema de gestão de estoque, 
informada abaixo entre os marcadores [INICIO] e [FIM], analise a seguinte entrada de usuário para 
determinar a ação desejada e forneça o código de comando correspondente. Use a descrição e o comando 
associado para fazer a melhor correspondência possível.

Não responda absolutamente nada além do código de comando correspondente ou "0" caso não encontre.
Se você não localizar um código correspondente retorne o valor "0". 
Se o seu grau de confiança na identificação da ação desjada for menor que 90%, retorne o valor "0".
Não inclua explicações adicionais, nem complementares, ou nenhum outro tipo de informação.

Entrada do Usuário:
{texto}

Tabela de de-para de comandos:
[INICIO]
{tabela}
[FIM]
"""

def prepara_prompt():
    prompt = PromptTemplate(
        template=PROMPT_BASE,
        input_variables=["texto", "tabela"],
    )
    return prompt
