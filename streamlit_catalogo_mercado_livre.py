#PEGANDO O NÚMERO DE ANÚNCIOS NO CATALOGO DO MERCADO LIVRE 
import pandas as pd 
import requests
import streamlit as st 
import base64

## Função 

#Download do arquivo 
def get_dataset(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}">Download em csv</a>'
    
    return st.markdown(href, unsafe_allow_html=True)

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
    
    #Mostrando o total de anúncios 
    st.write("Há o total de **{}** de anúncios deste produto no catálogo".format(catalogy['paging']['total']))
    
    #Criando variavél e lista 
    ids = []

    i = 0 

    for item in catalogy['results']:
        ids.append(catalogy['results'][i]['item_id'])
        i = i + 1
    
    #Criando a variavél e pegando os preços dos anúncios
    price = []
    
    p = 0 
    
    for item in catalogy['results']:
        price.append(catalogy['results'][p]['price'])
        p = p + 1        

    #Criando variavél para pegar os ids dos sellers 
    n = 0 

    sellers_id = []

    for item in catalogy['results']:
        sellers_id.append(catalogy['results'][n]['seller_id'])
        n = n + 1

    #Criando variavél para pegar os nomes dos sellers 

    n = 0 

    sellers_name = []

    for seller in sellers_id:
        r = requests.get('https://api.mercadolibre.com/users/{}'.format(sellers_id[n]))
        sellers = r.json()
        sellers_name.append(sellers['nickname'])
        n = n + 1 
    
    #Criando o dataframe 
    dataset = pd.DataFrame()

    #Colocando os dados 
    dataset['Ids'] = ids 
    dataset['Sellers'] = sellers_name
    dataset['Price'] = price

    #Mostrando o dataset 
    st.dataframe(dataset)
    
    #Fazendo o link para download
    get_dataset(dataset)
