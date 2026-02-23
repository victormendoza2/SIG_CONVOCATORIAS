from dashboard_generator import generar_dashboard
from remoteok_scraper import buscar_remoteok
from peru_gov_scraper import buscar_gob_peru
from excel_export import exportar_excel


# 🔎 Palabras clave reales (más estrictas)
PALABRAS_CLAVE = [
    # SIG reales
    "sistemas de información geográfica",
    "sistemas de informacion geografica",
    "arcgis",
    "qgis",
    "geoespacial",
    "cartografia",
    "cartografía",

    # Data específicos
    "analista de datos",
    "data analyst",
    "ciencia de datos",
    "power bi",

    # Consultoría
    "consultor",
    "consultoria",
    "consultoría",
    "tdr"
]

# ❌ Excluir basura
EXCLUIR = [
    "practica",
    "voluntariado",
    "ventas",
    "call center",
    "graphic designer",
    "ux",
    "ui",
    "marketing",
    "sales",
    "qa engineer",
    "c++",
    "frontend",
    "backend"
]


def clasificar_trabajo(texto):
    texto = texto.lower()

    sig_keywords = [
        "sistemas de información geográfica",
        "sistemas de informacion geografica",
        "arcgis",
        "qgis",
        "geoespacial",
        "cartografía",
        "cartografia"
    ]

    data_keywords = [
        "analista de datos",
        "data analyst",
        "ciencia de datos"
    ]

    if any(p in texto for p in sig_keywords):
        return "SIG"

    if "power bi" in texto:
        return "Power BI"

    if any(p in texto for p in data_keywords):
        return "Data"

    if any(p in texto for p in ["consultor", "consultoría", "consultoria", "tdr"]):
        return "Consultoría"

    return "Otros"


def clasificar_entidad(job):
    empresa = job.get("empresa", "").lower()
    link = job.get("link", "").lower()

    if any(p in empresa for p in [
        "ministerio",
        "municipalidad",
        "muni",
        "gobierno",
        "ana",
        "minam",
        "serfor",
        "cenepred",
        "gore"
    ]):
        return "Estado Perú"

    if any(p in empresa for p in [
        "ong",
        "fundación",
        "fundacion",
        "unicef",
        "pnud",
        "wwf"
    ]):
        return "ONG"

    if "teamtailor" in link:
        return "Privado - Portal"

    return "Privado"


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

    print("🚀 Buscando trabajos...")

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

    # 🔎 Aplicar filtro inteligente
    jobs_filtrados = filtro_inteligente(jobs_total)
    print(f"Después del filtro SIG/Data: {len(jobs_filtrados)}")

    # 🧠 Clasificar categoría y entidad
    for job in jobs_filtrados:
        texto = job.get("titulo", "") + " " + job.get("descripcion", "")
        job["categoria"] = clasificar_trabajo(texto)
        job["tipo_entidad"] = clasificar_entidad(job)

    # ❌ Eliminar categoría irrelevante
    jobs_filtrados = [j for j in jobs_filtrados if j["categoria"] != "Otros"]
    print(f"Después de eliminar Otros: {len(jobs_filtrados)}")

    # 📊 Exportar resultados
    exportar_excel(jobs_filtrados)
    generar_dashboard(jobs_filtrados)


if __name__ == "__main__":
    main()
