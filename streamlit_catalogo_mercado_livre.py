#PEGANDO O NÚMERO DE ANÚNCIOS NO CATALOGO DO MERCADO LIVRE 
import pandas as pd 
import requests
import streamlit as st 

# Criando a aplicação 
st.title("Buscador de ID de anúncios dentro do Catalogo do Mercado Livre")

#Criando o sidebar 
st.sidebar.title('Parâmetros de busca')

st.sidebar.write("Coloque o PRODUCT_ID que está na url do mercado Livre")

product_id = st.sidebar.text_input("Cole seu ID aqui")

#Criando o botão 
button = st.sidebar.button('Pegue os IDs')

if button: 
    #Fazendo o requests 
    r = requests.get('https://api.mercadolibre.com/products/{}/items#json'.format(product_id))

    #Lendo o JSON
    catalogy = r.json()

    #Fazendo a busca dos id 

    #Criando variavél e lista 
    ids = []

    i = 0 

    for item in catalogy['results']:
        ids.append(catalogy['results'][i]['item_id'])
        i = i + 1

    st.write(ids)