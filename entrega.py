import streamlit as st
import openai


# Función para generar contenido SEO utilizando OpenAI GPT-3.5
def generate_seo_content(api_key, keyword, content_type):
    openai.api_key = api_key
    prompt = f" Necesito que te comportes como un experto en posicionamiento SEO y me generes contenido SEO para el siguiento contenido {content_type} priorizando esta palabra clave '{keyword}'. La respuesta de esto tiene que ser directamente el contenido SEO segun el {content_type}. Ejemplo: Si el content_type = 'Title' mostrar solo el title en la respuesta. Teniendo en cuenta los caracteres sugeridos para cada uno de estos. 65 caracteres para el title, Entre 70 y 155 caracteres para la metadescription y los headings sean en una sola linea."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content'].strip()


# Configuración de la página de Streamlit
st.title('Generador de Contenido SEO con IA')
st.markdown('Esta aplicación genera Titles, Metadescriptions, H1 y H2 utilizando Inteligencia Artificial.')


# Campo para ingresar la API key
api_key = st.text_input('Introduce tu API Key de OpenAI:', type='password')


if api_key:
    # Campos de entrada para las keywords
    keyword = st.text_input('Introduce la keyword principal:')


    # Botones para generar los diferentes tipos de contenido SEO
    if keyword:
        st.subheader('Generación de Contenido SEO')
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button('Generar Title'):
                title = generate_seo_content(api_key, keyword, 'title')
                st.text_area('Generated Title:', title, height=100)
            
            if st.button('Generar H1'):
                h1 = generate_seo_content(api_key, keyword, 'H1')
                st.text_area('Generated H1:', h1, height=100)
        
        with col2:
            if st.button('Generar Metadescription'):
                metadescription = generate_seo_content(api_key, keyword, 'metadescription')
                st.text_area('Generated Metadescription:', metadescription, height=100)
            
            if st.button('Generar H2'):
                h2 = generate_seo_content(api_key, keyword, 'H2')
                st.text_area('Generated H2:', h2, height=100)
