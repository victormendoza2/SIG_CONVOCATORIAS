import pandas as pd
import os
from datetime import datetime

def generar_dashboard(jobs):

    if not jobs:
        print("No hay datos para dashboard.")
        return

    df = pd.DataFrame(jobs)

    os.makedirs("docs", exist_ok=True)

    fecha = datetime.now().strftime("%d/%m/%Y %H:%M")

    html_content = f"""
    <html>
    <head>
        <title>Dashboard Vacantes SIG</title>
        <style>
            body {{
                font-family: Arial;
                margin: 40px;
                background-color: #f5f5f5;
            }}
            h1 {{
                color: #2c3e50;
            }}
            table {{
                border-collapse: collapse;
                width: 100%;
                background: white;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 8px;
            }}
            th {{
                background-color: #2c3e50;
                color: white;
            }}
            tr:hover {{
                background-color: #f2f2f2;
            }}
        </style>
    </head>
    <body>
        <h1>Vacantes SIG / Data</h1>
        <p>Última actualización: {fecha}</p>
        {df.to_html(index=False, escape=False)}
    </body>
    </html>
    """

    with open("docs/index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("🌐 Dashboard generado en docs/index.html")
