import streamlit as st
import time
import os
from judini.codegpt.chat import Completion
import requests
import json
from PIL import Image
from semantic_router import Route
from semantic_router.encoders import CohereEncoder
from semantic_router.layer import RouteLayer
from dotenv import load_dotenv
load_dotenv()

api_key= os.getenv("CODEGPT_API_KEY")
agent_id= os.getenv("CODEGPT_AGENT_ID")
st.set_page_config(layout="centered")


# create the encoder
encoder = CohereEncoder()

# we could use this as a guide for our chatbot to avoid political conversations
emergencia = Route(
    name="ayuda_chile",
    utterances=[
        "¿Qué se sabe sobre la emergencia del incendio?",
        "¡La quinta región de Chile se está quemando!",
        "¿Está controlado el incendio en la quinta región?",
        "¿Cómo puedo ayudar con la emergencia del incendio en la quinta región?",
        "Cuéntame más sobre el incendio en la quinta región.",
        "¿Quién está luchando contra el incendio en la quinta región?",
        "¿Cómo comenzó el incendio en la quinta región?",
        "¿Cuánto daño ha causado el incendio en la quinta región?",
        "¿Existen planes de recuperación para la quinta región después del incendio?",
        "¿Cuánta gente ha sido afectada por el incendio en la quinta región?",
        "¿que centro de ayuda hay en santiago?",
        "¿Donde hay centros de Ayuda?",
        "Quiero ayudar",
        "Cómo puedo ayudar?",
        "Donde puedo ayudar?",
        "Quiero donar",
        "Cómo puedo donar?",
        "Donde puedo donar?",
        "Quiero hacer una donación",
        "Cómo puedo hacer una donación?",
        "Donde puedo hacer una donación?",
        "Quiero donar dinero",
        "Cómo puedo donar dinero?",
        "Donde puedo donar dinero?",
        "Quiero donar ropa",
        "Cómo puedo donar ropa?",
        "Donde puedo donar ropa?",
        "Quiero donar comida",
        "Cómo puedo donar comida?",
        "Donde puedo donar comida?",
        "Quiero donar medicinas",
        "Cómo puedo donar medicinas?",
        "Donde puedo donar medicinas?",
        "Quiero donar sangre",
        "Cómo puedo donar sangre?",
        "Donde puedo donar sangre?",
        "Quiero donar tiempo",
        "Cómo puedo donar tiempo?",
    ],
)

# creamos las rutas
routes = [emergencia]

# agrega dos columnas
col1, col2 = st.columns([2,3])

# columna 1 con la imagen
with col1:
    image = Image.open('assets/ayuda_chile_gpt_logo.png')
    st.image(image, width=200)

with col2:
    st.title("AyudaChile GPT 🤖🇨🇱")
    st.write("Soy un agente especialista en responder preguntas sobre centros de ayuda o actualizaciones del estado de emergencia en Chile. ")
    st.write("Estoy aquí para ayudarte en lo que necesites en relación a la emergencia")

st.write("Proyecto open-source: "+ "https://github.com/davila7/AyudaChileGPT")
st.markdown('---')

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("How can I help you?"):
    rl = RouteLayer(encoder=encoder, routes=routes)
    route = rl(prompt).name

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        with st.spinner('Cargando respuesta...'):
            message_placeholder = st.empty()
            full_response = ""
            messages = st.session_state.messages
            #st.write(route)
            if(route == 'ayuda_chile'):
                completion = Completion(api_key)
                response_completion = completion.create(agent_id, messages, stream=False)
            else:
                response_completion = "Estoy aquí para ayudarte en relación a la emergencia"
                
            for response in response_completion:
                time.sleep(0.05)
                full_response += (response or "")
                message_placeholder.markdown(full_response + "▌")       
            message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    
