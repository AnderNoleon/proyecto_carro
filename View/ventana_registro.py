from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, TableStyle

def create_pdf(filename):
    # Crea un nuevo archivo PDF con tamaño de página "carta"
    c = canvas.Canvas(filename, pagesize=letter)

    # Agrega el encabezado "Factura" centrado
    c.setFontSize(16)
    c.drawCentredString(300, 750, "Factura")

    # Agrega una línea gruesa debajo del encabezado
    c.setStrokeColorRGB(0, 0, 0)  # Color de línea negro
    c.setLineWidth(2)
    c.line(50, 730, 550, 730)

    # Agrega la información de la empresa a la izquierda del PDF con un tamaño de letra más pequeño
    c.setFontSize(10)
    c.drawString(50, 700, "Poseidón Cars 1/64")
    c.drawString(50, 685, "Séptima calle, 14 avenida zona 3")
    c.drawString(50, 670, "Quetzaltenango")
    c.drawString(50, 655, "Guatemala, Código Postal: 09010")

    # Obtiene la fecha y hora actuales
    now = datetime.now()
    # Formatea la fecha actual como string y la agrega al PDF con la leyenda "Fecha y hora de emisión:"
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    c.setFontSize(10)
    c.drawString(350, 700, "Fecha y hora de emisión:")
    c.setFontSize(10)
    c.drawString(350, 685, "{}".format(current_time))

    # Agrega una doble línea delgada debajo del encabezado
    c.setLineWidth(0.5)
    c.line(50, 640, 550, 640)
    c.line(50, 638, 550, 638)



    # Agrega el resto del contenido del PDF
    c.drawString(50, 600, "Nombre del cliente:")
    c.drawString(50, 580, "Dirección del cliente:")
    c.drawString(50, 560, "Ciudad, Estado, País, Código Postal:")

    c.drawString(50, 520, "Descripción del producto:")
    c.drawString(50, 500, "Precio unitario:")
    c.drawString(50, 480, "Cantidad:")
    c.drawString(50, 460, "Total:")

    data = [['Producto', 'Precio'],
            ['Producto 2', '$75'],
            ['Producto 3', '$100'],
            ['Producto 4', '$125']]

    # Define el tamaño de la tabla y los márgenes
    table = Table(data, colWidths=[300, 50])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
    ]))

    table.wrapOn(c, 50, 400)
    table.drawOn(c, 50, 400)

    # Guarda el PDF y cierra el canvas
    c.save()

# Crea un nuevo PDF llamado "factura.pdf" en la ruta especificada
create_pdf("E:\\Anderson\\Tareas\\Ciclo 3\\Investigacion\\proyecto_carro\\PDF\\factura.pdf")

