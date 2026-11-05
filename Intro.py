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

    st.markdown("## 🤖 GATO LABORATORIO")

    st.markdown("---")

    st.markdown("### Sobre este proyecto")

    st.write(
        """
        Esta plataforma reúne diferentes gatos super inteligentes que le saben mucho de todo
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
# =========================================================
# APLICACIONES
# =========================================================

st.markdown(
    '<div class="section-title">🚀 Aplicaciones disponibles</div>',
    unsafe_allow_html=True
)


apps = [

    {
        "title": "Gato primigenio",
        "category": "Testeo",
        "description": "Un gato que aprende a ser una app.",
        "image": "bb.jpg",
        "url": "https://prueba0-9aucmwwierqlcdttjh92nu.streamlit.app/"
    },
    {
        "title": "Conversión de texto a miaus",
        "category": "Audio · IA",
        "description": "Convierte texto escrito en voz utilizando modelos de Inteligencia Gatificial.",
        "image": "Meowing.jpg",
        "url": "https://iaolxrurxtue8evzceawxc.streamlit.app/"
    },

    {
        "title": "Reconocimiento de objetos con mirada felina",
        "category": "Visión artificial",
        "description": "Detecta y reconoce diferentes objetos presentes dentro de una imagen.",
        "image": "Analisis.jpg",
        "url": "https://tmq2ubj7plohcvehdqyrxg.streamlit.app/"
    },

    {
        "title": "Gato multilingue escribe y traduce tu voz",
        "category": "Audio · IA",
        "description": "Transforma una grabación de voz en texto utilizando reconocimiento automático.",
        "image": "Escucho.jpg",
        "url": "https://traductor-uubufkpcjuyhmdhkiu9w34.streamlit.app/"
    },

    {
        "title": "Gato atento",
        "category": "Reconocimiento de caracteres y audio",
        "description": "Un gato que lee y escribe (2 en 1 :0).",
        "image": "ojo.jpg",
        "url": "https://ocr-audio-mowrdsystlhkbu8wnp3p4m.streamlit.app/"
    },
   {
        "title": "Gato nuboso",
        "category": "Gato con nubes de palabras",
        "description": "Genera nubes de palabras para visualizar la frecuencia de de palabras claves.",
        "image": "cloud.jpg",
        "url": "https://wordcloud-373vsda7nssa25ct9h2vkr.streamlit.app/"
    },
       {
        "title": "Gato lector y analizador",
        "category": "Gato letrado",
        "description": "Analiza el texto que le pases, bastante paciente.",
        "image": "lee.jpg",
        "url": "https://lv6epjfenvoicubsfqsdeb.streamlit.app/"
    },
    {
        "title": "Gato cyborg",
        "category": "Gato IA",
        "description": "Con el poder de la IA identifica lo que le muestras.",
        "image": "yolo.jpg",
        "url": "https://yolov5-mszqk7zkmlqzijnivru4uf.streamlit.app/"
    },
    {
        "title": "Gato sabiondo",
        "category": "RAG · Documentos",
        "description": "Consulta documentos PDF utilizando al gato sabiondo.",
        "image": "gato.jpg",
        "url": "https://chatpdf1-pra6mueuxeefwd3ntynadu.streamlit.app//"
    },
  {
        "title": "Análisis de imagen",
        "category": "Computer Vision",
        "description": "Explora la capacidad de los modelos de IA para interpretar y analizar imágenes.",
        "image": "Miro.jpg",
        "url": "https://visionapp-zztkqkzpqxrkt8nvhqptbq.streamlit.app/#analisis-de-mirada-gatuna-de-imagen"
    },
      {
        "title": "Gato tablero",
        "category": "herramienta tablero",
        "description": "Gato equipado con un increible tablero.",
        "image": "tablero.jpg",
        "url": "https://tableromartin.streamlit.app/"
    },
    {
        "title": "Gato lector de sentimientos",
        "category": "IA · Mundo físico",
        "description": "Este gato siente lo que sientes",
        "image": "Sentimientos.jpg",
        "url": "https://sentimento-m7zcn3udu8dytjzgmkuglw.streamlit.app/"
    },
    {
        "title": "Gato Robot mueve pata",
        "category": "IA · Mundo físico",
        "description": "Este gato controla circuitos",
        "image": "robot cat.png",
        "url": "https://sendcmqtt-cxtbnvlyrem8vdmuf6ssvs.streamlit.app/"
    },
    {
        "title": "Sensor gatuno",
        "category": "IA · Mundo físico",
        "description": "Este gato siente las variables",
        "image": "gatosensor.jpg",
        "url": "https://recepmqtt-crtomtybmcdbaeep2p2rnh.streamlit.app/"
    },
       {
        "title": "Gato telefono",
        "category": "Escucha control",
        "description": "Este gato da ordenes con tu voz",
        "image": "sing.jpg",
        "url": "https://ctrlvoice-86mdj52mep8iksbiatodzf.streamlit.app/"
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
