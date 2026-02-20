from dashboard_generator import generar_dashboard
from remoteok_scraper import buscar_remoteok
from peru_gov_scraper import buscar_gob_peru
from excel_export import exportar_excel

# 🔎 Palabras clave SIG / Data
PALABRAS_CLAVE = [
    "sig", "gis", "arcgis", "qgis",
    "power bi", "analisis de datos",
    "data analyst", "geoespacial",
    "cartografia", "consultor", "consultoria"
]

# ❌ Excluir
EXCLUIR = [
    "practica", "voluntariado",
    "ventas", "call center"
]

def clasificar_trabajo(texto):
    texto = texto.lower()

    # SIG / GIS fuerte
    if any(p in texto for p in [
        "sistemas de informacion geografica",
        "sistema de informacion geografica",
        "geografica",
        "geoespacial",
        "arcgis",
        "qgis",
        "gis",
        "sig",
        "cartografia"
    ]):
        return "SIG"

    # Power BI
    if "power bi" in texto:
        return "Power BI"

    # Data
    if any(p in texto for p in [
        "analista de datos",
        "data analyst",
        "ciencia de datos",
        "data science",
        "analisis de datos"
    ]):
        return "Data"

    # Consultoría
    if any(p in texto for p in [
        "consultor",
        "consultoria",
        "términos de referencia",
        "tdr"
    ]):
        return "Consultoría"

    return "Otros"
    
def filtro_inteligente(jobs):
    filtrados = []

    for job in jobs:
        texto = (
            job.get("titulo", "") + " " +
            job.get("descripcion", "")
        ).lower()

        if any(p in texto for p in PALABRAS_CLAVE) and not any(e in texto for e in EXCLUIR):
            filtrados.append(job)

    return filtrados


def main():

    print("🚀 Buscando trabajos multipágina...")

    jobs_total = []

    # 🔹 RemoteOK
    jobs_remote = buscar_remoteok()
    print(f"RemoteOK encontrados: {len(jobs_remote)}")
    jobs_total.extend(jobs_remote)

    # 🔹 Gob Perú
    jobs_gob = buscar_gob_peru()
    print(f"Gob Perú encontrados: {len(jobs_gob)}")
    jobs_total.extend(jobs_gob)

    print(f"Total encontrados: {len(jobs_total)}")

    # 🔎 Aplicar filtro
    jobs_filtrados = filtro_inteligente(jobs_total)

    print(f"Después del filtro SIG/Data: {len(jobs_filtrados)}")

    # 🧠 🔥 AQUI agregamos categoría
    for job in jobs_filtrados:
        texto = job.get("titulo", "") + " " + job.get("descripcion", "")
        job["categoria"] = clasificar_trabajo(texto)

    # 📊 Exportar
    exportar_excel(jobs_filtrados)
    generar_dashboard(jobs_filtrados)


if __name__ == "__main__":
    main()
