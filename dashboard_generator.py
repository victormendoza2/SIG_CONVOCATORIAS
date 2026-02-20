import pandas as pd
import os
from datetime import datetime

def generar_dashboard(jobs):

    if not jobs:
        print("No hay datos para dashboard.")
        return

    df = pd.DataFrame(jobs)

    # Crear columna de enlace clickeable
    if "link" in df.columns:
        df["URL"] = df["link"].apply(lambda x: f'<a href="{x}" target="_blank">Ver oferta</a>')

    os.makedirs("docs", exist_ok=True)

    fecha = datetime.now().strftime("%d/%m/%Y %H:%M")

    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Dashboard Vacantes SIG / Data</title>

        <!-- DataTables CSS -->
        <link rel="stylesheet" href="https://cdn.datatables.net/1.13.5/css/jquery.dataTables.min.css">

        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 20px;
                background: #f5f5f5;
            }}
            h1 {{
                color: #2c3e50;
            }}
        </style>
    </head>
    <body>
        <h1>📊 Vacantes – SIG / Data / Consultoría</h1>
        <p>Última actualización: {fecha}</p>

        <table id="jobsTable" class="display" style="width:100%">
            <thead>
                <tr>
                    <th>Título</th>
                    <th>Empresa</th>
                    <th>Categoría</th>
                    <th>URL</th>
                </tr>
            </thead>
            <tbody>
    """

    for _, row in df.iterrows():
        titulo = row.get("titulo", "")
        empresa = row.get("empresa", "")
        categoria = row.get("categoria", "")
        url_html = row.get("URL", "")

        html_template += f"""
            <tr>
                <td>{titulo}</td>
                <td>{empresa}</td>
                <td>{categoria}</td>
                <td>{url_html}</td>
            </tr>
        """

    html_template += """
            </tbody>
        </table>

        <!-- jQuery -->
        <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
        <!-- DataTables JS -->
        <script src="https://cdn.datatables.net/1.13.5/js/jquery.dataTables.min.js"></script>

        <script>
            $(document).ready(function() {
                $('#jobsTable').DataTable({
                    "pageLength": 10
                });
            });
        </script>
    </body>
    </html>
    """

    with open("docs/index.html", "w", encoding="utf-8") as f:
        f.write(html_template)

    print("🌐 Dashboard interactivo generado en docs/index.html")
