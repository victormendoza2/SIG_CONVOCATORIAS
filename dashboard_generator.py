import os
from datetime import datetime

def generar_dashboard(jobs):

    # Si no hay trabajos, generar dashboard vacío profesional
    if not jobs:
        html = """
        <html>
        <head>
            <meta charset="UTF-8">
            <title>SIG Convocatorias</title>
        </head>
        <body>
            <h1>No se encontraron vacantes hoy</h1>
            <p>El sistema se actualizó correctamente.</p>
            <p>Fecha: {}</p>
        </body>
        </html>
        """.format(datetime.now().strftime("%d/%m/%Y %H:%M"))

        os.makedirs("docs", exist_ok=True)

        with open("docs/index.html", "w", encoding="utf-8") as f:
            f.write(html)

        return

    # Si sí hay trabajos
    contenido = ""

    for job in jobs:
        contenido += f"""
        <div style="border:1px solid #ccc; padding:10px; margin:10px;">
            <h2>{job.get('titulo')}</h2>
            <p><b>Empresa:</b> {job.get('empresa')}</p>
            <a href="{job.get('link')}" target="_blank">Ver más</a>
        </div>
        """

    html = f"""
    <html>
    <head>
        <meta charset="UTF-8">
        <title>SIG Convocatorias</title>
    </head>
    <body>
        <h1>Convocatorias SIG & Data</h1>
        <p>Actualizado: {datetime.now().strftime("%d/%m/%Y %H:%M")}</p>
        {contenido}
    </body>
    </html>
    """

    os.makedirs("docs", exist_ok=True)

    with open("docs/index.html", "w", encoding="utf-8") as f:
        f.write(html)
