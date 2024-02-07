import streamlit as st
import streamlit.components.v1 as components
import os
from judini.codegpt.chat import Completion
import requests
from PIL import Image
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

# set API Key
codegpt_api_key= os.getenv("CODEGPT_API_KEY")
# Set API base URL
codegpt_api_base = os.getenv("CODEGPT_API_BASE")
#set API base dev URL
codegpt_api_base_dev = os.getenv("CODEGPT_API_BASE_DEV")

# set ID de Agentes
codegpt_acopio_agent_id= os.getenv("CODEGPT_ACOPIO_AGENT_ID")
codegpt_fibe_agent_id= os.getenv("CODEGPT_FIBE_AGENT_ID")

st.set_page_config(layout="centered")

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

def page1():
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("Consulta sobre la emergencia"):

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

                # semantic router
                # Rutas semanticas para detectar saludos
                payload = {
                    "route_names": [
                        "greetings"
                    ],
                    "prompt": prompt
                }
                
                # Realiza la solicitud POST
                url = codegpt_api_base_dev+"/labs/semantic_route_by_names"
                response_route = requests.post(url, json=payload)
                
                # Inicializa el completion
                completion = Completion(codegpt_api_key)
                # Verificar si la solicitud fue exitosa
                if response_route.status_code == 200:
                    # La respuesta de la solicitud es un JSON, así que usamos .json() para decodificarlo
                    data = response_route.json()

                    # Validar que ruta tomar
                    if data.get("route") == "greetings":
                        response_completion = iter(["Realiza cualquier consulta sobre la emergencia en Chile"])
                    else:
                        response_completion = completion.create(codegpt_acopio_agent_id, messages, stream=True)
                        
                else:
                    # si hay error en el servicio de RAG se envía al modelo
                    response_completion = completion.create(codegpt_acopio_agent_id, messages, stream=True)
                
                for response in response_completion:
                    full_response += (response or "")
                    message_placeholder.markdown(full_response + "▌") 
                message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})

def page2():
    st.header("Centros de ayuda verificados")

    # Cargar el archivo csv
    @st.cache_data
    def load_data():
        return pd.read_csv('assets/centros_verificados_v5_urls.csv')

    # Cargar los datos
    df = load_data()

    # Incrustar el mapa de Google Maps
    map_url = "https://www.google.com/maps/d/embed?mid=13KKV0Sy81G2L0Vz5lS9E90YysNi71BQ&ehbc=2E312F&noprof=1"
    components.iframe(map_url, width=640, height=480)


    # Tabla de datos
    # estilos
    style = """
    <style>
        .dataframe {
            border-collapse: collapse;
            padding: 10px;
            width: 100%;
        }
        .dataframe th, .dataframe td {
            border: 1px solid #ddd;
            padding: 8px;
        }
        @media screen and (max-width: 600px) {
            .dataframe tr {
                border-bottom: none !important;
            }
            .dataframe td {
                border-bottom: 1px solid #ddd;
            }
        }
    </style>
    """


    # Input de texto 
    filtro = st.text_input('Filtrar información')

    # Filtrar el dataframe 
    df_filtered = df[df.apply(lambda row: row.astype(str).str.lower().str.contains(filtro.lower()), axis = 1).any(axis = 1)]

    # Mostrar el dataframe
    if not df_filtered.empty:
        # Crear una nueva columna con enlaces HTML
        df_filtered['Mapa enlace'] = df_filtered['Mapa'].apply(lambda x: f'<a target="_blank" href="{x}">{x}</a>')
        # Drop y rename columna Mapa
        df_filtered = df_filtered.drop(columns=['Mapa']).rename(columns={'Mapa enlace': 'Mapa'})

        # Mostrar el DataFrame con enlaces 
        st.write(df_filtered.to_html(escape=False), unsafe_allow_html=True)
    else:
        st.write("No se encontraron resultados para el filtro aplicado.")

def page3():
    st.title('Mapa de la Nasa con focos de incendios')
    st.write('Fuente: https://firms.modaps.eosdis.nasa.gov/')
    
    # --------------------- Process data from NASA ---------------------------
    import datetime
    # Get the current date
    current_date = datetime.date.today()

    # Format the date as 'YYYY-MM-DD'
    formatted_date = current_date.strftime('%Y-%m-%d')

    # Construct the URL with the formatted date
    url = f"https://firms.modaps.eosdis.nasa.gov/api/country/csv/c45d84bcde5bf60dcb80b3c44983536a/VIIRS_NOAA20_NRT/CHL/1/{formatted_date}"

    # Read the data from the URL
    df = pd.read_csv(url)

    # If the dataframe is empty, get the data from the previous day
    if df.empty:
        previous_date = current_date - datetime.timedelta(days=1)
        previous_formatted_date = previous_date.strftime('%Y-%m-%d')
        previous_url = f"https://firms.modaps.eosdis.nasa.gov/api/country/csv/c45d84bcde5bf60dcb80b3c44983536a/VIIRS_NOAA20_NRT/CHL/1/{previous_formatted_date}"
        df = pd.read_csv(previous_url)

    # Rename columns to 'lat' and 'lon'
    df = df.rename(columns={'latitude': 'lat', 'longitude': 'lon'})

    # Convert bright_ti4 and bright_ti5 to Celsius
    df['bright_ti4'] = df['bright_ti4'] - 273.15
    df['bright_ti5'] = df['bright_ti5'] - 273.15

    # Convert acq_date and acq_time to datetime
    df['acq_time'] = pd.to_datetime(df['acq_time'], format='%H%M%S').dt.time

    # --------------------------- GET UTC CHile Time---------------------------
    import pytz
    from datetime import datetime, timedelta

    # Set the timezone for Chile
    chile_timezone = pytz.timezone('Chile/Continental')

    # Get the current UTC time
    current_utc_time = datetime.now(pytz.utc)

    # Convert the UTC time to Chile timezone
    chile_time = current_utc_time.astimezone(chile_timezone)

    # Get the -03 from the timezone offset
    timezone_offset = chile_time.strftime('%z')
    timezone_offset = timezone_offset[:3]

    # Convert timezone_offset to an integer
    timezone_offset = int(timezone_offset)

    # If timezone_offset is negative, multiply by -1
    if timezone_offset < 0:
        timezone_offset *= -1

    # Create a timedelta object with the timezone offset
    td = timedelta(hours=timezone_offset)

    # ---------------------------- Convert UTC to Chile Time ----------------------------
    df['acq_time'] = pd.to_datetime(df['acq_time'], format='%H:%M:%S').dt.time
    # Subtract timedelta
    df['acq_time'] = pd.to_datetime(df['acq_time'], format='%H:%M:%S') - td
    # Extract time component
    df['acq_time'] = df['acq_time'].dt.time

    # Get a variable to show in the app
    info_updated_time = df['acq_time'].max().strftime('%H:%M:%S')
    info_updated_date = df['acq_date'].max()
    
    # --------------------------- Show the data in a map using Streamlit ---------------------------
    st.write(f"Última actualización satelital: {info_updated_date} - {info_updated_time} (hora local de Chile)")

    # Mostrar los datos en un mapa usando Streamlit
    st.map(df)

def page4():
    # st.title("EN CONSTRUCCIÓN")
    # Aquí va todo el contenido de la página 4
    # Propuesta para cargar datos de un excell y que sean extraidos datos de personas desapareciddas. 
    # By Computer Science Engineer : Felipe Alfonso Gonzalez - github.com/felipealfonsog 
    st.title("Lista de personas desaparecidas")

    # URL del archivo Excel en la nube
    excel_url = "assets/personas_desaparecidas.csv"

    # Cargar los datos desde el Excel en la nube
    try:
        df = pd.read_excel(excel_url)

        # Filtro de personas confirmadas
        confirmadas_only = st.checkbox("Mostrar solo personas confirmadas")
        if confirmadas_only:
            df = df[df['Estado'].str.contains('Confirmado', case=False, na=False)]

        st.write("Datos de personas desaparecidas:")
        st.write(df)
    except Exception as e:
        st.write(f"Error al cargar los datos del Excel: {e}")

def page5():
    st.header("Establecimientos Habilitados Mineduc")
    st.write("Fuente: https://www.mineduc.cl/reporte-mineduc-por-incendios-establecimientos-apoyan-la-emergencia/")

    # Cargar el archivo csv
    @st.cache_data
    def load_data():
        return pd.read_csv('assets/authorized_establishments.csv')

    # Cargar los datos
    df = load_data()

    filter = st.text_input('Filtrar información')

    df = df[df.apply(lambda row: row.astype(str).str.lower().str.contains(filter.lower()), axis=1).any(axis=1)]

    st.write(df)
        
#sidebar
PAGES = {
    "Chat AyudaChileGPT": page1,
    "Centros de Ayuda Verificados": page2,
    "Mapa de Incendios": page3,
    # "Personas Desaparecidas": page4,
    "Establecimientos Habilitados Mineduc": page5
}

st.sidebar.title('Navegación')
selection = st.sidebar.radio("Ir a", list(PAGES.keys()))
page = PAGES[selection]

# Mostrar la página seleccionada con el radio button
page()






