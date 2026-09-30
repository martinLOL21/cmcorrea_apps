import streamlit as st
from PIL import Image
from textwrap import dedent

# =========================================================
# CONFIGURACIÓN
# =========================================================

st.set_page_config(
    page_title="Aplicaciones de Inteligencia Artificial",
    page_icon="🤖",
    layout="wide"
)


# =========================================================
# CSS
# =========================================================

st.markdown(dedent("""
<style>

    /* =========================
       FONDO
       ========================= */

    .stApp {
        background:
            radial-gradient(
                circle at 10% 10%,
                rgba(224, 93, 240, 0.12),
                transparent 30%
            ),
            radial-gradient(
                circle at 90% 20%,
                rgba(93, 121, 240, 0.12),
                transparent 30%
            ),
            #0D0B18;

        color: #F5F3FF;
    }


    /* =========================
       SIDEBAR
       ========================= */

    section[data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #17112B 0%,
            #100E1D 100%
        );

        border-right: 1px solid rgba(144, 100, 227, 0.25);
    }

    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #E05DF0;
    }


    /* =========================
       HERO
       ========================= */

    

    .hero-label {
        display: inline-block;

        padding: 7px 15px;

        border-radius: 50px;

        background: rgba(109, 97, 250, 0.18);

        color: #C061FA;

        font-size: 13px;

        font-weight: 700;

        letter-spacing: 1px;

        margin-bottom: 15px;
    }

    .main-title {
        font-size: 48px;

        font-weight: 800;

        line-height: 1.1;

        background: linear-gradient(
            90deg,
            #E05DF0,
            #C061FA,
            #6D61FA,
            #5D79F0
        );

        -webkit-background-clip: text;

        -webkit-text-fill-color: transparent;

        margin-bottom: 15px;
    }

    .subtitle {
        color: #B9B4CC;

        font-size: 18px;

        max-width: 800px;

        line-height: 1.6;
    }


    /* =========================
       TÍTULOS
       ========================= */

    .section-title {
        font-size: 28px;

        font-weight: 700;

        color: #F5F3FF;

        margin-top: 30px;

        margin-bottom: 20px;
    }


    /* =========================
       TARJETAS
       ========================= */

    div[data-testid="stVerticalBlockBorderWrapper"] {

        background: rgba(25, 21, 43, 0.85);

        border: 1px solid rgba(144, 100, 227, 0.30);

        border-radius: 20px;

        transition: all 0.25s ease;

        padding: 5px;
    }

    div[data-testid="stVerticalBlockBorderWrapper"]:hover {

        border-color: rgba(192, 97, 250, 0.7);

        box-shadow:
            0 10px 35px rgba(109, 97, 250, 0.18);

        transform: translateY(-3px);
    }


    /* =========================
       TEXTO DE LAS TARJETAS
       ========================= */

    .card-category {

        color: #5D79F0;

        font-size: 12px;

        font-weight: 700;

        text-transform: uppercase;

        letter-spacing: 1px;

        margin-top: 10px;
    }

    .card-title {

        color: #FFFFFF;

        font-size: 21px;

        font-weight: 700;

        margin-top: 5px;
    }

    .card-description {

        color: #AAA5BC;

        font-size: 14px;

        line-height: 1.6;

        min-height: 65px;
    }


    /* =========================
       BOTONES
       ========================= */

    div.stButton > button,
    div[data-testid="stLinkButton"] a {

        border-radius: 12px !important;

        border: none !important;

        background: linear-gradient(
            90deg,
            #9064E3,
            #6D61FA
        ) !important;

        color: white !important;

        font-weight: 700 !important;

        transition: all 0.2s ease;
    }

    div.stButton > button:hover,
    div[data-testid="stLinkButton"] a:hover {

        background: linear-gradient(
            90deg,
            #E05DF0,
            #C061FA
        ) !important;

        transform: translateY(-2px);
    }


    /* =========================
       RECURSOS
       ========================= */

    .resource-box {

        padding: 25px;

        border-radius: 18px;

        background:
            linear-gradient(
                135deg,
                rgba(224, 93, 240, 0.10),
                rgba(93, 121, 240, 0.10)
            );

        border: 1px solid rgba(109, 97, 250, 0.3);

        margin-bottom: 15px;
    }

    .resource-title {

        font-size: 21px;

        font-weight: 700;

        color: #C061FA;

        margin-bottom: 8px;
    }

</style>
"""), unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## 🤖 IA LAB")

    st.markdown("---")

    st.markdown("### Sobre este proyecto")

    st.write(
        """
        Esta plataforma reúne diferentes aplicaciones y
        experimentos desarrollados utilizando técnicas de
        Inteligencia Artificial.
        """
    )

    st.markdown("### ¿Qué encontrarás?")

    st.markdown("""
    🔊 Texto y voz

    👁️ Visión artificial

    📊 Análisis de datos

    📝 Procesamiento de lenguaje

    🧠 Modelos de IA

    📄 RAG y documentos

    ⚙️ Sistemas inteligentes
    """)

    st.markdown("---")

    st.caption("Proyecto académico · Inteligencia Artificial")


# =========================================================
# HERO
# =========================================================

st.markdown(dedent("""
<div class="hero">

    <div class="hero-label">
        LABORATORIO DE INTELIGENCIA ARTIFICIAL
    </div>

    <div class="main-title">
        Explora las posibilidades de la IA
    </div>

    <div class="subtitle">
        Una colección de aplicaciones y experimentos que
        muestran diferentes formas en las que la Inteligencia
        Artificial puede utilizarse para transformar texto,
        imágenes, audio y datos.
    </div>

</div>
"""), unsafe_allow_html=True)


# =========================================================
# RECURSOS
# =========================================================

st.markdown(dedent("""
<div class="resource-box">

    <div class="resource-title">
        🌐 Explora más ejercicios
    </div>

    <div>
        Encuentra páginas adicionales y ejercicios prácticos
        relacionados con Inteligencia Artificial.
    </div>

</div>
"""), unsafe_allow_html=True)

st.link_button(
    "Abrir colección de ejercicios →",
    "https://sites.google.com/view/aplicacionesdeia/inicio"
)


# =========================================================
# APLICACIONES
# =========================================================

st.markdown(
    '<div class="section-title">🚀 Aplicaciones disponibles</div>',
    unsafe_allow_html=True
)


apps = [

    {
        "title": "Conversión de texto a voz",
        "category": "Audio · IA",
        "description": "Convierte texto escrito en voz utilizando modelos de Inteligencia Artificial.",
        "image": "txt_to_audio2.png",
        "url": "https://imultimod.streamlit.app/"
    },

    {
        "title": "Reconocimiento de objetos",
        "category": "Visión artificial",
        "description": "Detecta y reconoce diferentes objetos presentes dentro de una imagen.",
        "image": "txt_to_audio.png",
        "url": "https://yolov5cmc.streamlit.app/"
    },

    {
        "title": "Entrenando modelos",
        "category": "Machine Learning",
        "description": "Explora cómo utilizar un modelo entrenado para realizar tareas de reconocimiento.",
        "image": "OIG5.jpg",
        "url": "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/"
    },

    {
        "title": "Conversión de voz a texto",
        "category": "Audio · IA",
        "description": "Transforma una grabación de voz en texto utilizando reconocimiento automático.",
        "image": "OIG8.jpg",
        "url": "https://traductorw.streamlit.app/"
    },

    {
        "title": "Análisis de datos",
        "category": "Datos · IA",
        "description": "Analiza conjuntos de datos mediante herramientas y agentes basados en IA.",
        "image": "data_analisis.png",
        "url": "https://dataagente.streamlit.app/"
    },

    {
        "title": "Transcriptor de audio y video",
        "category": "Procesamiento de audio",
        "description": "Obtén transcripciones de archivos de audio y video mediante modelos de reconocimiento.",
        "image": "OIG3.jpg",
        "url": "https://transcript-whisper.streamlit.app/"
    },

    {
        "title": "Generación en contexto",
        "category": "RAG · Documentos",
        "description": "Consulta documentos PDF utilizando una aplicación basada en Retrieval Augmented Generation.",
        "image": "Chat_pdf.png",
        "url": "https://chatpdf-cc.streamlit.app/"
    },

    {
        "title": "Análisis de imagen",
        "category": "Computer Vision",
        "description": "Explora la capacidad de los modelos de IA para interpretar y analizar imágenes.",
        "image": "OIG4.jpg",
        "url": "https://vision2-gpt4o.streamlit.app/"
    },

    {
        "title": "Sistema ciberfísico",
        "category": "IA · Mundo físico",
        "description": "Experimenta con sistemas capaces de interactuar con información proveniente del mundo físico.",
        "image": "OIG6.jpg",
        "url": "https://vision2-gpt4o.streamlit.app/"
    }
]


# =========================================================
# GENERAR TARJETAS
# =========================================================

for i in range(0, len(apps), 3):

    columns = st.columns(3)

    for j, app in enumerate(apps[i:i+3]):

        with columns[j]:

            # ESTA ES LA PARTE IMPORTANTE
            # Ahora usamos un container real de Streamlit

            with st.container(border=True):

                # Imagen
                try:

                    image = Image.open(app["image"])

                    st.image(
                        image,
                        use_container_width=True
                    )

                except:

                    st.warning(
                        f"No se encontró la imagen: {app['image']}"
                    )

                # Categoría
                st.markdown(
                    f'<div class="card-category">{app["category"]}</div>',
                    unsafe_allow_html=True
                )

                # Título
                st.markdown(
                    f'<div class="card-title">{app["title"]}</div>',
                    unsafe_allow_html=True
                )

                # Descripción
                st.markdown(
                    f'<div class="card-description">{app["description"]}</div>',
                    unsafe_allow_html=True
                )

                # Botón
                st.link_button(
                    "Explorar aplicación →",
                    app["url"],
                    use_container_width=True
                )


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown(
    """
    <div style="
        text-align:center;
        color:#77718C;
        padding:20px;
    ">
        Laboratorio de Inteligencia Artificial ·
        Aplicaciones y experimentos
    </div>
    """,
    unsafe_allow_html=True
)
