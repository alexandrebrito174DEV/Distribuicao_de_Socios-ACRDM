from fastapi import FastAPI
from pydantic import BaseModel

# import random - posso fazer mas é melhor SERIAL na Base de Dados

app=FastAPI() #inicio da api - diz que estamos a querer criar a api
class UtilizadorACriar (BaseModel):


    nome: str
    perfil: str
    mensagem: str
    email: str

class UtilizadorSocio (UtilizadorACriar):
        id_socio: int
        telefone: str
        idade: int
        morada: str


@app.get("/") #rota inicial

def start():
    """devolve uma mensagem de inicio"""
    return {"mensagem inicial de first api": "Incio da minha Api em Python"}

#--------------------------------------------------------------------------------------------

@app.get("/sobre_esta_api")
def sobre():
   return {"mensagem acerca da api:": "Versão nº1",
           "Descrição": "Inicio da api muito simples"
           }

#cuidado com a indentação, isto não é C

#-------------------------------------------------------------------------------------------
@app.get("/socio/{id_socio}")
def mostrar(id_socio: int):
    return {
        "id socio": id_socio,
        "nome_socio": "Alexandre Dev",
        "email": "xxx@gmail.com",
        "mensagem": "Informações acerca do Sócio estão a ser apresentadas"

            }

@app.get("/socios")
def mostrar_geral():


    return{
        #socios  - nao deixa em parte de ser especie de um array de dados que consegue agrupar
        # mais do que um conjunto pessoal de dados

        # --- dicionario ---
        "socios": [
            {
        "id_socio": 1,
        "nome_socio": "Alexandre",
        "email": "alexandrebrito174@gmail.com",
        "telefone": "+351 924023383"
            },
            {
        "id_socio": 3,
        "nome_socio": "Maria",
        "email": "www@gmail.com",
        "telefone": "+351 000000000"
            }
    ],
         "mensagem_i": "Informação de todos os sócios adicionados foi apresentada no ecrã"

    # --- fim de dicionário ---
    }

# "socios" é uma chave do dicionário.
# O valor dessa chave é uma lista de dicionários,
# onde cada dicionário representa um sócio.

@app.post("/socio")
def criar_socio(Socio: UtilizadorACriar):
    return {
        "id_socio": 1,
        "nome_socio": Socio.nome,
        "email": Socio.email,
        "telefone": Socio.telefone,
        "mensagem": Socio.mensagem,
        "perfil": Socio.perfil,
    }
@app.put("/socios/{id_socio}") #usar um caminho reutilizavel devo usar {id_socio}
def atualizar_socios(id_socio: int):
    return {
        "id_socio": id_socio, #o id deve ser sempre o mesmo - não se altera o id
        "nome_socio": "Alexandre Brito DEV",
        "email": "alexandrebrito@gmail.com",
        "telefone": "+351 912345678",
        "Informações atualizadas": f"As informações (todas as infromações) acerca do Sócio {id_socio} foi atualizada"
        #Quando usamos um parametro e a sua variavel numa mensagem devemos efetivamnete colocar o "f" antes da mensagem
    }


@app.patch("/socios/{id_socio}")
# Patch - Atualização parcial de um ou mais campos do sócio
def atualizar_dados(id_socio: int): #id_socio como parametro para tornar reutilizavel
    return {
        "id_socio": id_socio, #reproveitar o id que vem da rota e da função (apresentado nos dois)
        "nome_socio": "Alexandre - O Grande DEV",
        "email": "alexandrebrito_dev@gmail.com",
        "telefone": "+351 924000000",
        f"Informações atualizadas": "As informações acerca do Sócio {id_socio} foi atualizada"
    } #importante colocar o 'f' para em parte chamar e apresentar o valor de determinada variavel


#-------------------------------------------------------------------------------
#------- Parte de Admin (DADOS) ---------
@app.get("/admin")
def admin():
    return {
        "id_admin": 1,
        "nome_admin": "Alexandrina Cunha",
        "email": "qqqq@gmail.com",
        "telefone": "+351 111111111",
        "função": "Administradora da gestão de Sócios da ACRDM"
    }
@app.post("/admin")
def criar_admin():
    return {
        "id_admin": 1,
        "nome_admin": "Alexandrina Cunha",
        "email": "qqqq@gmail.com",
        "telefone": "+351 111111111",
        "função": "Administradora da gestão de Sócios da ACRDM"
    }
@app.patch("/admin")
def atualizar_admin():
    return {
        "id_admin": 1,
        "nome_admin": "Alexandrina Cunha",
        "email": "cccc@gmail.com",
        "telefone": "+351 111111000",
        "função": "Administradora da gestão de Sócios "
    }
#----------------------------------------------------------------

#--- Parte de DEV ---
@app.get("/admin_dev")
def mostrar_dev():
    return {
        "id_admin_dev": 1,
        "nome_admin_dev": "Alexandre Brito",
        "email": "alexandre_dev@acrdm.pt",
        "função": "Administrador da parte técnica de Gestão de Sócios da ACRDM"
    }

@app.post("/admin_dev")
def criar_dev():
    return {
    "id_admin_dev": 1,
    "nome_admin_dev": "Alexandre Brito",
    "email": "alexandre_dev@acrdm.pt",
    "função": "Administrador da parte técnica de Gestão de Sócios da ACRDM"
    }
#-----------------------
# futuramente a inserção de algum tipo de dados é opcional, como EMAIL