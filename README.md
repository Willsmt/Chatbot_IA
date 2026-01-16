
```markdown
# Chatbot com IA PsychologistRaq 🧠💬

Este projeto é um chatbot interativo construído com **Streamlit** e integrado à API da **OpenAI**.  
O objetivo é criar uma interface simples onde o usuário envia mensagens e recebe respostas da IA em tempo real.  

---

## 🚀 Funcionalidades
- Campo de input para o usuário digitar mensagens.
- Exibição das mensagens enviadas pelo usuário.
- Envio da pergunta para a IA (OpenAI).
- Exibição da resposta da IA diretamente na tela.
- Histórico de mensagens mantido durante a sessão.

---

## 🛠️ Tecnologias utilizadas
- [Streamlit](https://streamlit.io/) → Frontend e backend em Python.
- [OpenAI](https://platform.openai.com/) → Modelo de linguagem (ChatGPT).
- [LangChain](https://www.langchain.com/) → Biblioteca para trabalhar com IA (opcional).
- [Hugging Face](https://huggingface.co/) → Para criar e hospedar seu próprio modelo de IA (opcional).

---

## 📦 Instalação

Clone este repositório:
```bash
git clone https://github.com/seuusuario/chatbot-ia.git
cd chatbot-ia
```

Instale as dependências:
```bash
pip install streamlit openai
```

---

## 🔑 Configuração da chave da OpenAI
No arquivo `secrets.toml` do Streamlit, adicione sua chave da OpenAI:

```toml
[general]
api_key = "SUA_CHAVE_OPENAI_AQUI"
```

---

## ▶️ Como rodar
Execute o comando abaixo no terminal:
```bash
streamlit run app.py
```

---

## 🌐 Teste Online
Você também pode testar o chatbot diretamente pelo deploy no Streamlit:  
👉 [Acesse aqui](https://chatbotia-rt4yngu88gi3iwocby8e5c.streamlit.app/)

---

---

## 📂 Estrutura do projeto
```
├── main.py              # Código principal do chatbot
├── README.md           # Documentação do projeto
├── .gitignore          # Arquivos ignorados pelo Git
└── requirements.txt    # Dependências do projeto
```

---

## 🧑‍💻 Exemplo de uso
1. Digite sua mensagem no campo de input.  
2. O chatbot exibirá sua mensagem.  
3. A IA processará e retornará uma resposta.  
4. O histórico da conversa será mostrado na tela.  

---

## 🧩 Futuras melhorias
- Integração com **LangChain** para fluxos mais complexos.  
- Treinamento de modelos próprios via **Hugging Face**.  
- Personalização de avatares para usuário e assistente.  

---

## 📝 Licença
Este projeto é de uso livre para fins educacionais e experimentais.  

