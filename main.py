#titulo
#input do chat (campo de mensagem)
# a cada mensam que o usuario enviar:
    #mostrar a mensagem que o usuario enviou no chat
    #pegar a perguntar e enviar para uma ia responder
    #exibir a resposta da ia na tela 

# streamlit -> apenas com python criar o front end e o backend
#a Ia que vamos usar: OpneAI (chatgpt)
#pip install streamlit openai

#HUGGING FACE - PARA CRIAR SEU PROPRIO MODELO DE IA

#LANGCHAIN - BIBLIOTECA PARA TRABALHAR COM IA 

#testando o gitignore

import streamlit as st
from openai import OpenAI

modelo_ia = OpenAI(api_key = st.secrets["api_key"])  #coloque sua chave da openai aqui 

st.write("# Chatbot com IA PsychologistRaq") #markdown -  formatacao de texto

if not "listas_de_mensagens" in st.session_state:
    st.session_state["listas_de_mensagens"] = []

texto_usuario = st.chat_input("Digite sua mensagem:")

for mensagem in st.session_state["listas_de_mensagens"]:
    #role = user, assistant  role=mensagem["role"]
    #content = conteudo da mensagem conteudo=mensagem["content"]
    st.chat_message(mensagem["role"]).write(mensagem["content"])

if texto_usuario:
    st.chat_message("user").write(texto_usuario)
    mensagem_usuario = {"role":"user", "content":texto_usuario}
    st.session_state["listas_de_mensagens"].append(mensagem_usuario)

#nome - aparece a primeira letra do nome
#user - foto do usuario 
#assistant - foto do assistente(ia)


#Ia resposta
    resposta_ia = modelo_ia.chat.completions.create(
    model="gpt-5-nano",
    messages=st.session_state["listas_de_mensagens"],
)
    texto_resposta_ia = resposta_ia.choices[0].message.content
    st.chat_message("assistant").write(texto_resposta_ia) 
    mensagem_ia = {"role":"assistant", "content":texto_resposta_ia}
    st.session_state["listas_de_mensagens"].append(mensagem_ia)


