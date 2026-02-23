import requests

def buscar_gob_peru():

    resultados = []

    try:
        url = "https://www.gob.pe/busquedas?contenido=convocatorias"
        r = requests.get(url, timeout=20)

        if r.status_code == 200:
            resultados.append({
                "fuente": "GobPeru",
                "titulo": "Convocatorias Estado Peruano",
                "empresa": "Estado Peruano",
                "link": url,
                "descripcion": "Revisión manual recomendada"
            })

    except:
        pass

    return resultados
