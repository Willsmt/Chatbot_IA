#listas

nomes =["ana","bia","carlos","daniel"]  # sempre para chiar uma lista usa colchetes []
print(nomes[0])  #acessar o elemento da lista - indice começa do 0
nomes.append("eduardo")  #adicionar um elemento na lista
print(nomes)

#dicionarios

# voce pode adicionar varios tipos de dados em um dicionario
# dicionario estrutura = {chave: valor, chave2: valor2, ...}
idades = {"ana":25, "bia":30, "carlos":22}
print(idades["bia"])  #acessar o valor pela chave # pegar informacao do dicionario - dicionario[chave]

# adicionar informacao no dicionario
idades["daniel"] = 28
print(idades)

# se voce tenta colocar uma chave que ja existe, o valor sera atualizado
idades["ana"] = 26
print(idades)

# se voce tentar colocar uma chave que nao existe, ela sera criada
idades["eduardo"] = 24  
print(idades)


#role = quem é o usuario (user, assistant, system)

mensagem1 = {"role":"user", "content":"Olá, como vai?"}
mensagem2 = {"role":"assistant", "content":"Estou bem, obrigado!"}  
mensagem3 = {"role":"user", "content":"Você é um assistente útil."}

listas_de_mensagens = [mensagem1, mensagem2, mensagem3]  # lista de dicionarios

nova_mensagem = {"role":"assistant", "content":"Fico feliz em ajudar!"}
listas_de_mensagens.append(nova_mensagem)