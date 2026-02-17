import requests

def main():
    print("🚀 Iniciando búsqueda de trabajos...")

    url = "https://remoteok.com/api"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        print(f"✅ Datos recibidos: {len(data)} registros")

        count = 0

        for job in data:
            title = str(job.get("position", "")).lower()

            if any(k in title for k in ["gis", "data", "analyst", "excel", "bi"]):
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
