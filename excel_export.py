import pandas as pd
import os

HISTORIAL_FILE = "historial.csv"

def exportar_excel(jobs):

    if not jobs:
        print("No hay trabajos para procesar.")
        return

    df_nuevos = pd.DataFrame(jobs)

    # Si no existe historial lo crea
    if not os.path.exists(HISTORIAL_FILE):
        df_nuevos[["Link"]].rename(columns={"Link": "link"}).to_csv(HISTORIAL_FILE, index=False)
        df_nuevos.to_excel("trabajos_nuevos.xlsx", index=False)
        print("📂 Historial creado.")
        return

    df_historial = pd.read_csv(HISTORIAL_FILE)

    # Comparar por link
    nuevos = df_nuevos[~df_nuevos["Link"].isin(df_historial["link"])]

    if nuevos.empty:
        print("🔁 No hay trabajos nuevos.")
        return

    # Guardar nuevos en Excel
    nuevos.to_excel("trabajos_nuevos.xlsx", index=False)

    # Actualizar historial
    df_actualizado = pd.concat([
        df_historial,
        nuevos[["Link"]].rename(columns={"Link": "link"})
    ])

    df_actualizado.drop_duplicates(inplace=True)
    df_actualizado.to_csv(HISTORIAL_FILE, index=False)

    print(f"🆕 Trabajos nuevos encontrados: {len(nuevos)}")
    print("📊 Excel generado con trabajos nuevos.")
