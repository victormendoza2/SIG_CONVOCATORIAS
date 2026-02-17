import pandas as pd

def exportar_excel(lista_jobs):

    if len(lista_jobs) == 0:
        return

    df = pd.DataFrame(lista_jobs)

    df.to_excel("trabajos_encontrados.xlsx", index=False)

    print("📊 Excel generado")
