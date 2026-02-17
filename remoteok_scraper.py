import requests

def buscar_remoteok():

    url = "https://remoteok.com/api"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    jobs_list = []

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        for job in data:

            title = str(job.get("position", ""))
            company = str(job.get("company", ""))
            link = str(job.get("url", ""))
            desc = str(job.get("description", ""))

            jobs_list.append({
                "fuente": "RemoteOK",
                "titulo": title,
                "empresa": company,
                "link": link,
                "descripcion": desc
            })

    except:
        pass

    return jobs_list
