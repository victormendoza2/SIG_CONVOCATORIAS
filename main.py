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

    jobs = buscar_trabajos()

print(f"Total encontrados: {len(jobs)}")

jobs_filtrados = filtro_inteligente(jobs)

print(f"Después del filtro SIG/Data: {len(jobs_filtrados)}")

exportar_excel(jobs_filtrados)

    print(f"Total encontrados: {len(jobs_total)}")

    exportar_excel(jobs_total)


if __name__ == "__main__":
    main()

