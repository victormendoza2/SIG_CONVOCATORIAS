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

    # 📊 Exportar
    exportar_excel(jobs_filtrados)
    generar_dashboard(jobs_filtrados)


if __name__ == "__main__":
    main()
