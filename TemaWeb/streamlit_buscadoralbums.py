import streamlit as st
from fuzzywuzzy import fuzz

album = [
    {
        "track_id": 1,
        "title": "Song of the Dawn",
        "authors": ["Alice Johnson", "Michael Lee", "Sophia Walker"],
        "duration": 3.45
    },
    {
        "track_id": 2,
        "title": "Echoes of Time",
        "authors": ["Brian Adams"],
        "duration": 4.20
    },
    {
        "track_id": 3,
        "title": "Mystic Nights",
        "authors": ["Clara Smith", "David Thompson", "Olivia Brown"],
        "duration": 5.10
    },
    {
        "track_id": 4,
        "title": "Beyond Horizons",
        "authors": ["Emma Davis", "George Martin", "Sophia Taylor"],
        "duration": 4.05
    },
    {
        "track_id": 5,
        "title": "Whispers in the Wind",
        "authors": ["George Martin", "Sophia Taylor", "Liam Harris"],
        "duration": 3.55
    }
]

def get_min_cancion(album):
    return min([cancion["duration"] for cancion in album])

def get_max_cancion(album):
    return max([cancion["duration"] for cancion in album])

st.title("🎈 Buscador de canciones")
st.write(
    "Bienvenidos a mi buscador de canciones.."
)

resultado = st.text_input("¿Qué canción buscas?")
ratio = 0
closest = {}
if resultado:
    for cancion in album:
        x = fuzz.ratio(resultado.lower(), cancion["title"].lower())
        if x > ratio:
            ratio = x
            closest = cancion

    st.write(f"{closest} con un ratio de {ratio}")


option = st.selectbox(
    "Introducir una opción:", 
    ["Canción más corta", "Canción más larga"]  
)

match option:
    case "Canción más corta":
        duracion = get_min_cancion(album)
        st.write(f"La canción que dura menos es {duracion}")
    case "Canción más larga":
        duracion = get_max_cancion(album)
        st.write(f"La canción que dura más es {duracion}")
    case _:
        st.write("Invalid selection.")
