from dotenv import load_dotenv
import os

from langchain_text_splitters import Language

# Load environment variables from .env file
load_dotenv()

# Access an environment variable
api = os.getenv('API_KEY')


from langchain_groq import ChatGroq 
from langchain.prompts import ChatPromptTemplate

chat = ChatGroq(model='llama3-8b-8192', api_key=api)

def respostas_bot(mes, doc):
    mensagens_modelo = [("system", "Você é um assistente amigavel chamado BW, você utiliza as seguintes informações para formular suas respostas: {inf}, para encerrar a conversa, o usuario deve digitar x")]
    mensagens_modelo += mes
    template = ChatPromptTemplate.from_messages(mensagens_modelo)
    chain = template | chat
    return chain.invoke({"inf": doc}).content


from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import YoutubeLoader
from langchain_community.document_loaders import PyPDFLoader

def carrega_site():
    url_site = input("Digite a url do site: ")
    doc = ""
    loader = WebBaseLoader(url_site)
    list_doc = loader.load()
    for i in list_doc:
        doc += i.page_content
    return doc

def carrega_pdf():
    print("Atualmente apenas é possivel ler pdfs inseridos no código \n Vá até o comando 'carrega_pdf' e adicone o caminho para o pdf local que deseja utilizar")
    doc = ""
    caminho = "./Profissional.pdf" #Coloque o caminho para o pdf local
    loader = PyPDFLoader(caminho)
    list_doc = loader.load()
    for i in list_doc:
        doc += i.page_content
    return doc

def carrega_yotube():
    url = input("Digite a url do video: ")
    doc = ""
    loader = YoutubeLoader.from_youtube_url(
        url,
        language=['pt']
    )
    list_doc = loader.load()
    for i in list_doc:
        doc += i.page_content
    return doc


    
print("Bem-vindo ao BW, seu assistente amigavel")

while True:
    
    selecao = input(''' Digite 1 se quiser conversar com um site
 Digite 2 se quiser conversar com um PDF
 Digite 3 se quiser conversar com um video no youtube 
 Valor: ''')
    
    if (selecao == '1'):
        doc = carrega_site()
        break
    elif selecao == "2":
        doc = carrega_pdf()
        break
    elif selecao == "3":
        doc = carrega_yotube()
        break
    else:
        print("Digite um valor valido \n")
        

mensagens = []       
while True:
    mes = input("Usuario: ")
    if mes == "x":
        break
    mensagens.append(("user", mes))
    res = respostas_bot(mensagens, doc)
    mensagens.append(("assistant", res))
    print(f"Bot: {res}")
    
print("Muito obrigado por usar o BW")
        
        
        



