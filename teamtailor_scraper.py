import requests

def buscar_teamtailor():
    urls = [
        "https://ocaglobal.teamtailor.com/jobs.json"
    ]

    jobs = []

    for url in urls:
        try:
            r = requests.get(url, timeout=10)
            data = r.json()

            for job in data.get("jobs", []):
                jobs.append({
                    "titulo": job.get("title"),
                    "empresa": "OCA Global",
                    "descripcion": job.get("description", ""),
                    "link": job.get("url")
                })
        except:
            pass

    return jobs
