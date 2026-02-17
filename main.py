import requests

def main():
    print("🚀 Iniciando búsqueda de trabajos...")

    url = "https://remoteok.com/api"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    # =============================
    # KEYWORDS PRO
    # =============================

    tech_keywords = [
        "gis","sig",
        "excel",
        "power bi","powerbi",
        "data","analytics",
        "python",
        "remote",
        "analyst","analysis"
    ]

    latam_keywords = [
        "peru","chile","colombia","mexico",
        "argentina","ecuador","bolivia",
        "latam","latin america"
    ]

    gov_keywords = [
        "cenepred","serfor","ana",
        "ministerio","ministry",
        "municipalidad","municipality",
        "gobierno regional"
    ]

    consult_keywords = [
        "consultoria","consultoría",
        "tdr",
        "convocatoria",
        "cas",
        "locacion de servicios"
    ]

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        print(f"✅ Datos recibidos: {len(data)} registros")

        count = 0

        for job in data:

            title = str(job.get("position", "")).lower()
            description = str(job.get("description", "")).lower()

            text_total = title + " " + description

            tech_match = any(k in text_total for k in tech_keywords)
            latam_match = any(k in text_total for k in latam_keywords)
            gov_match = any(k in text_total for k in gov_keywords)
            consult_match = any(k in text_total for k in consult_keywords)

            if tech_match or latam_match or gov_match or consult_match:
                print("-----")
                print("Trabajo:", job.get("position"))
                print("Empresa:", job.get("company"))
                print("Link:", job.get("url"))
                count += 1

        print(f"\n🎯 Trabajos filtrados encontrados: {count}")

    except Exception as e:
        print("❌ ERROR GENERAL:", str(e))


if __name__ == "__main__":
    main()
