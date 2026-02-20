import pandas as pd
import os
from datetime import datetime

def generar_dashboard(jobs):

    if not jobs:
        print("No hay datos para dashboard.")
        return

    df = pd.DataFrame(jobs)

    # Convertir links en botones
    if "link" in df.columns:
        df["Ver"] = df["link"].apply(
            lambda x: f'<a href="{x}" target="_blank">🔗 Ver</a>'
        )

    os.makedirs("docs", exist_ok=True)

    fecha = datetime.now().strftime("%d/%m/%Y %H:%M")

    html_content = f"""
    <html>
    <head>
        <title>Dashboard SIG / Data</title>
        <style>
            body {{
                font-family: Arial;
                margin: 40px;
                background-color: #f4f6f9;
            }}
            h1 {{
                color: #1f2d3d;
            }}
            .card {{
                background: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            }}
            table {{
                border-collapse: collapse;
                width: 100%;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }}
            th {{
                background-color: #1f2d3d;
                color: white;
            }}
            tr:hover {{
                background-color: #f1f1f1;
            }}
            a {{
                text-decoration: none;
                font-weight: bold;
            }}
        </style>
    </head>
    <body>

        <h1>📊 Vacantes SIG / Data / Consultoría</h1>
        <p>Última actualización: {fecha}</p>

        <div class="card">
            {df.to_html(index=False, escape=False)}
        </div>

    </body>
    </html>
    """

    with open("docs/index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("🌐 Dashboard mejorado generado.")
