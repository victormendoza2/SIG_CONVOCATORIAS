import requests
from bs4 import BeautifulSoup

def buscar_gob_peru():

    resultados = []

    try:
        url = "https://www.gob.pe"
        r = requests.get(url, timeout=20)

        soup = BeautifulSoup(r.text, "html.parser")

        textos = soup.get_text().lower()

        keywords = [
            "convocatoria",
            "consultoria",
            "tdr",
            "servicios"
        ]

        if any(k in textos for k in keywords):

            resultados.append({
                "fuente": "GobPeru",
                "titulo": "Posible convocatoria detectada",
                "empresa": "Estado Peruano",
                "link": url,
                "descripcion": "Detectado por palabras clave"
            })

    except:
        pass

    return resultados
