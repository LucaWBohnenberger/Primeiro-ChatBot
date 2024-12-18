# 🤖 ChatBot Analisador de Conteúdo

Este projeto é um chatbot desenvolvido para analisar conteúdos de vídeos do YouTube, arquivos PDF e sites, utilizando a biblioteca LangChain. Este é um projeto de estudos e a primeira vez que desenvolvo um chatbot! 🚀

## ⚠️ Avisos
- 🛠️ **Para o funcionamento correto, é necessário clonar o repositório e adicionar um arquivo `.env` com uma chave de API da Groq da seguinte forma:**
  `API_KEY = {Chave}` 
- 📄 **A função de ler PDFs funciona somente com PDFs adicionados manualmente no código, pois é apenas um chat de terminal. Para adicionar, procure a função `carregar_pdf()` e adicione o caminho para o PDF que deseja ler.** 


## ✨ Funcionalidades

- 📹 **Análise de Vídeos do YouTube:** Extrai e interpreta informações de vídeos para responder perguntas e fornecer resumos.
- 📄 **Processamento de Arquivos PDF:** Lê e analisa arquivos PDF, permitindo consultas sobre seu conteúdo.
- 🌐 **Exploração de Sites:** Realiza buscas e extrai dados relevantes de sites para responder perguntas específicas.

## 🛠️ Tecnologias Utilizadas

- **[LangChain](https://www.langchain.com/):** Framework principal para construção do chatbot.
- **Python:** Linguagem de programação utilizada.
- **APIs Externas:** Para acesso e análise de conteúdo online.

## 🚀 Como Executar o Projeto

 1. **Clone o repositório:**
    ```bash
    git clone https://github.com/LucaWBohnenberger/Primeiro-ChatBot.git
    ```

 2. **Acesse o diretório:**
    ```bash
    cd Primeiro-ChatBot
    ```

 3. **Instale as dependências:**
    ```bash
    python projeto.py
    ```
