from remoteok_scraper import buscar_remoteok
from peru_gov_scraper import buscar_gob_peru
from excel_export import exportar_excel


def main():

    print("🚀 Buscando trabajos multipágina...")

    jobs_total = []

    jobs_total += buscar_remoteok()
    jobs_total += buscar_gob_peru()

    print(f"Total encontrados: {len(jobs_total)}")

    exportar_excel(jobs_total)


if __name__ == "__main__":
    main()

