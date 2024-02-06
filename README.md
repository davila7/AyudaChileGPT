### AyudaChileGPT 🤖
Agente IA Open-Source para atender consultas sobre la emergencia en Chile 🚨 🇨🇱

[![AyudaChileGPT Badge](https://custom-icon-badges.demolab.com/badge/AyudaChileGPT-blue.svg?logo=ayudachilegpt4&logoColor=white&style=plastic)](#)

<sub>
  
- Website Oficial: [ayudachilegpt.cl](http://ayudachilegpt.cl/)

- Enlace al agente:  [Ayuda Chile GPT en onrender.com](https://ayuda-chile-gpt.onrender.com/)

- Donaciones a [Desafío Levantemos Chile](https://desafiolevantemoschile.org/) (Fundación de Apoyo a la Ciudadanía y Emergencias en Chile)

- Donaciones a Fundación [Un Techo para Chile](https://cl.techo.org/)

</sub>
<br>

<!--
<img width="977" alt="Captura de pantalla 2024-02-04 a las 08 36 41" src="https://github.com/davila7/AyudaChileGPT/assets/6216945/16cdfa24-6cd9-41df-821a-66a34bd874ad">
-->


| ![Logo](/assets/logo_v2_square.jpg) | <h6>Agente IA con información verificada sobre la emergencia en Chile, [¿Cómo ayudar?](#c%C3%B3mo-ayudar-)<br><br> - Mejora en el código fuente, el proyecto es Open Source. <br> - Agrega y/o verifica información en el GDrive de archivos. <br> - Comparte el agente! </h6> |
| :--- | :--- |

[![Twitter](https://img.shields.io/badge/Compartir%20en-Twitter-blue?logo=twitter&style=plastic)](https://twitter.com/intent/tweet?url=http://ayudachilegpt.cl/&text=AyudaChileGPT%20en%20Twitter&&hashtags=chile,auidachilegpt,chileayuda,emergencia)
[![Facebook](https://img.shields.io/badge/Compartir%20en-Facebook-blue?logo=facebook&style=plastic)](https://www.facebook.com/sharer/sharer.php?u=http://ayudachilegpt.cl/)
[![LinkedIn](https://img.shields.io/badge/Compartir%20en-LinkedIn-blue?logo=linkedin&style=plastic)](https://www.linkedin.com/shareArticle?url=http://ayudachilegpt.cl/&title=AyudaChileGPT%20en%20LinkedIn&summary=AyudaChileGPT%20en%20LinkedIn)

![Main Language](https://img.shields.io/github/languages/top/davila7/AyudaChileGPT.svg?style=flat&color=blue)
[![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

#### Descripción 🔍

AyudaChileGPT es un agente de Inteligencia Artificial que permite responder preguntas relacionadas con la emergencia en Chile. El agente utiliza la tecnología de procesamiento del lenguaje natural mediante la API de 
[CodeGPT](https://developers.codegpt.co) para entender las preguntas y proporcionar respuestas precisas y útiles.

El objetivo de AyudaChileGPT es proporcionar información actualizada y confiable sobre la emergencia en Chile, ayudando a las personas a obtener respuestas rápidas y precisas a sus preguntas.


#### ¿Cómo ayudar? 🚀
Puedes ayudar realizando las siguientes acciones:

- Puedes agregar un [PR](#contribuciones-a-trav%C3%A9s-de-pull-requests) al proyecto si quieres mejorar las funcionalidades del Agente.
- Puedes agregar archivos de conocimiento a la base de datos en esta carpega en Google Drive: [DB GDrive](https://bit.ly/BD-GDrive)
  
  ```
  https://bit.ly/BD-GDrive
  ```
  
- Comparte el link del Agente para que más personas puedan tener acceso a la información actualizada sobre la emergencia que está sufriendo Chile 🇨🇱

##### ¿Cómo usar? 🤔

Instala las siguientes librerías
```
pip install -r requirements
```

- Streamlit: Esta librería se utiliza para crear una interfaz de usuario interactiva para el agente AyudaChileGPT.
- Judini: Esta librería se utiliza para procesar el lenguaje natural mediante la API de [CodeGPT](https://developers.codegpt.co) y generar respuestas precisas a las preguntas del usuario.

Una vez que hayas instalado las librerías, puedes ejecutar el agente AyudaChileGPT utilizando el siguiente comando:

```
streamlit run ayuda_chile_gpt.py
```

Esto abrirá una interfaz de usuario en tu navegador web. Simplemente escribe tu pregunta en el campo de texto y presiona el botón "Enviar". El agente procesará tu pregunta y te proporcionará una respuesta en la sección de resultados.

##### Funcionalidades ⚙️

- Respuestas precisas: AyudaChileGPT utiliza la tecnología de procesamiento del lenguaje natural para entender las preguntas y proporcionar respuestas precisas y útiles.
- Información actualizada: El agente se actualiza constantemente con información actualizada sobre la emergencia en Chile para proporcionar respuestas precisas y confiables.
- Interfaz de usuario interactiva: AyudaChileGPT cuenta con una interfaz de usuario interactiva y fácil de usar, lo que lo hace accesible para cualquier persona que necesite información sobre la emergencia en Chile.
- Amplia gama de preguntas: El agente está diseñado para responder una amplia gama de preguntas relacionadas con la emergencia en Chile, desde información sobre recursos y ayuda hasta medidas de prevención y estadísticas.
- Accesibilidad: AyudaChileGPT está disponible en línea y es accesible desde cualquier dispositivo con conexión a internet, lo que lo hace fácil de usar para cualquier persona que necesite información sobre la emergencia en Chile.

##### Pendientes ⚙️

1. Conectar con APIs que entreguen el estado actual de los incendios
2. Conectar con API que entregue la calidad del aire
3. Conectar con API que permitan realizar donaciones
4. Conectar con API que proporcionen informaciones sobre los refugios disponibles para emergencias
5. Implementar funcionalidad de alertas en tiempo real para informar a los usuarios sobre situaciones de emergencia
6. Conectar con API que proporcione una lista de números de contacto de emergencia locales
7. Mejorar la capacidad de hacer preguntas sobre la base de datos de emergencias.

##### 🤝 Soporte y Contribuciones 🤝

Si encuentras útil este proyecto y deseas apoyar su desarrollo, hay varias formas en las que puedes contribuir:

- **Contribuciones de Código**: Si eres un desarrollador, puedes contribuir enviando pull requests con correcciones de errores, nuevas características o mejoras. Siéntete libre de bifurcar el proyecto y crear tu propia rama para trabajar en ella.
- **Informes de Errores y Retroalimentación**: Si encuentras algún problema o tienes sugerencias para mejorar, por favor abre un problema en el repositorio de GitHub del proyecto. Tu retroalimentación es valiosa para hacer que el proyecto sea mejor.
- **Documentación**: Siempre se aprecia mejorar la documentación. Si encuentras alguna laguna o tienes sugerencias para mejorar la documentación del proyecto, puedes informarlo.

#### Contribuciones a través de Pull Requests*

¡Las contribuciones son bienvenidas! Aquí te explicamos cómo puedes contribuir a Term Notes:

1. Haz un fork del repositorio.
2. Crea una nueva rama: `git checkout -b caracteristica/nombre-de-tu-caracteristica`.
3. Realiza tus cambios y compromételos: `git commit -m 'Agregar tu característica'`.
4. Sube los cambios a tu rama: `git push origin caracteristica/nombre-de-tu-caracteristica`.
5. Crea una nueva solicitud de Pull Request.


##### Versión ChatGPT 🏷️
En la versión ChatGPT, el agente AyudaChileGPT se ha mejorado para proporcionar una experiencia de chat más interactiva y conversacional. El agente ahora puede mantener una conversación más fluida con el usuario, lo que lo hace más accesible y fácil de usar.
AyudaChile GPT 🤖 🇨🇱 en [ChatGPT](https://chat.openai.com/g/g-G3TvxWdjN-ayudachile-gpt)


#### 📄 License 📄

This project is licensed under the [MIT License](LICENSE).

<sub>Developed from Chile and for Chile with :heart:</sub>

