from fastapi import FastAPI #import necessário - vai importar algo da biblioteca
# import random - posso fazer mas é melhor SERIAL na Base de Dados
app=FastAPI() #inicio da api - diz que estamos a querer criar a api
@app.get("/") #rota inicial

def start():
    """devolve uma mensagem de inicio"""
    return {"mensagem inicial de first api" "Incio da minha Api em Python"}

#--------------------------------------------------------------------------------------------

@app.get("/sobre_esta_api")
def sobre():
   return {"mensagem acerca da api:": "Versão nº1/n Descrição: Inicio da api muito simples"}

#cuidado com a indentação, isto não é C

#-------------------------------------------------------------------------------------------
@app.get("/socio_id")
def mostrar():
    return {
        "id socio": 2,
        "nome_socio": "Alexandre Dev",
        "email": "xxx@gmail.com",
        "mensagem": "Informações acerca do Sócio estão a ser apresentadas"

            }

@app.get("/socios")
def mostrar_geral():

    def informacao_mensagem():
        return {
            "mensagem": "Informação de todos os sócios foi apresentada no ecrã"
        }

    return{
        #socios  - nao deixa em parte de ser especie de um array de dados que consegue agrupar
        # mais do que um conjunto pessoal de dados

        # --- dicionario ---
        "socios": [
            {
        "id_socio": 1,
        "nomes_socio": "Alexandre",
        "email": "alexandrebrito174@gmail.com",
        "telefone": "+351 924023383"
            },
            {
        "id_socio": 3,
        "nome_socio": "Maria",
        "email": "www@gmail.com",
        "telefone": "+351 000000000"
            }
    ]
    # --- fim de dicionário ---
    }

# "socios" é uma chave do dicionário.
# O valor dessa chave é uma lista de dicionários,
# onde cada dicionário representa um sócio.

@app.post("/socio_id")
def criar_socio():
    return {
        "id_socio": 1,
        "nome_socio": "Alexandre",
        "email": "alexandrebrito174@gmail.com",
        "telefone": "+351 924023383"
    }
@app.put("/socios/{id_socio}") #usar um caminho reutilizavel devo usar {id_socio}
def atualizar_socios():
    return {
        "id_socio": 1, #o id deve ser sempre o mesmo - não se altera o id
        "nome_socio": "Alexandre Brito DEV",
        "email": "alexandrebrito@gmail.com",
        "telefone": "+351 912345678"
    }

@app.patch("/socios/{id_socio}")
# Patch - Atualização parcial de um ou mais campos do sócio
def atualizar_dados(id_socio: int): #id_socio como parametro para tornar reutilizavel
    return {
        "id_socio": id_socio, #reproveitar o id que vem da rota e da função (apresentado nos dois)
        "nome_socio": "Alexandre - O Grande DEV",
        "email": "alexandrebrito_dev@gmail.com",
        "telefone": "+351 924000000"
    }


#-------------------------------------------------------------------------------
#------- Parte de Admin (DADOS) ---------
@app.get("/admin")
def admin():
    return {
        "id_admin": 1,
        "nome_admin": "Alexandrina",
        "email": "qqqq@gmail.com",
        "telefone": "+351 111111111"
    }
app.post("/admin")
def criar_admin():
    return {
        "id_admin": 1,
        "nome_admin": "Alexandrina",
        "email": "qqqq@gmail.com",
        "telefone": "+351 111111111"
    }
#----------------------------------------

# futuramente a inserção de algum tipo de dados é opcional, como EMAIL