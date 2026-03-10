import random
import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors

# 1. LLISTA DE CANÇONS (Les 90 que has passat)
cancons = [
    "Euphoria - Loreen", "Queen of kings - Alessandra", "No dudaria - Antonio Flores",
    "Superestrella - Aitana", "Cuentame - Ana Belén", "La Perla - Rosalía",
    "Flowers - Miley Cyrus", "Sweet Caroline - Dj Ötzy", "Titanium - David Guetta",
    "Un petonet - The tyets", "Eso que tú me das - Jarabe De Palo", "Livin' On A Prayer - Bon Jovi",
    "Una Foto en Blanco y Negro - El Canto Del Loco", "NUEVAYoL - Bad Bunny", "Abre Tu Mente - Merche",
    "La Mujer de Verde - IZAL", "Mescalina - Los Rebeldes", "Veo Veo - Teresa Rabal",
    "Madre Tierra - Chayanne", "Shake It Off - Taylor Swift", "Wannabe - Spice Girls",
    "The Time of My Life - Bill Medley", "Tobogan - Zoo", "Vagabundo - Sebastian Yatra",
    "Un Beso - Nueva Línea", "Sexbomb - Tom Jones", "Quiero Decirte - Abraham Mateo",
    "Galilea - Sergio Dalma", "Let it Be - The Beatles", "I Will Survive - Gloria Gaynor",
    "Te Amaré - Miguel Bosé", "Santa Lucia - Miguel Rios", "La Lola - Café Quijano",
    "Estoy Por Ti - Amistades Peligrosas", "Amores de Barra - Ella Baila Sola", "In The Navy - Village People",
    "Todos Me Miran - Gloria Trevi", "El Sol No Regresa - La Quinta Estacion", "La Gent Que Estimo - Oques Grasses",
    "Y Yo Sigo Aquí - Paulina Rubio", "Besos en Guerra - Morat", "Can't Stop The Feeling! - Justin Timberlake",
    "Como Yo Te Amo - Rocio Jurado", "No Es Serio Este Cementerio - Mecano", "Dramas Y Comedias - Fangoria",
    "Los Dos Cogidos de la Mano - Alejandro Sanz", "Mujer de las Mil Batallas - Manuel Carrasco", "Si te vas... - Extremoduro",
    "Sin Ti No Soy Nada - Amaral", "Bohemian Rhapsody - Queen", "What's Up? - 4Non Blondes",
    "Dancing Queen - Abba", "Un Beso Y Una Flor - Nino bravo", "Ave Maria - David Bisbal",
    "Puedes Contar Conmigo - La Oreja de Van Gogh", "Azul - Cristian Castro", "Fruta Fresca - Carlos Vives",
    "Serà porque te amo - Dj Matrix", "Madrid City - Ana Mena", "El Mambo - Kiko Rivera",
    "Uno Más Uno son 7 - Fran Perea", "Tanto la Queria - Andy & Lucas", "Color Esperanza - Diego Torres",
    "A fuego lento - Rosana", "Viva la Vida - Coldplay", "Alocao - Omar Montes",
    "Me has invitado a bailar - Dani Fernández", "Libertad - Nil Moliner", "Soldadito Marinero - Fito y Fitipaldis",
    "Carolina - M-Clan", "Peter Pan - El Canto del Loco", "Don't Wanna Miss a Thing - Aerosmith",
    "Hawái - Maluma", "Blanco y Negro - Malú", "Laura No Está - Nek",
    "Cuando Zarpa el Amor - Camela", "Búscate un hombre que te quiera - El Arrebato", "Física o Química - Despistaos",
    "Total Eclipse of the Heart - Bonnie Tyler", "Like a Prayer - Madonna", "What a feeling - Irene Cara",
    "Unchained Melody - The Righteous Brothers", "La Vida Es Un Carnaval - Celia Cruz", "Torero - Chayanne",
    "Eva Maria - Formula V", "Miénteme - David Bisbal", "Estoy Hecho de Pedacitos de ti - Antonio Orozco",
    "Dos Hombres Y Un Destino - Bustamante", "La Barbacoa - Georgie Dann", "Lo Siento - Beret"
]

def generar_cartro_logic():
    # Crea la lògica de 15 cançons (5 per fila) en un graellat de 3x9
    indices = list(range(90))
    seleccio = random.sample(indices, 15)
    seleccio.sort()
    
    cartro = [[None for _ in range(9)] for _ in range(3)]
    puntuacions = [0] * 9
    
    # Repartir cançons per columnes (aproximat a bingo real)
    for idx in seleccio:
        col = idx // 10
        if col > 8: col = 8
        fila = random.randint(0, 2)
        while cartro[fila][col] is not None or sum(x is not None for x in cartro[fila]) >= 5:
            fila = (fila + 1) % 3
        cartro[fila][col] = cancons[idx]
    return cartro

def dibuixar_pdfs(num_inici, num_final, nom_arxiu):
    c = canvas.Canvas(nom_arxiu, pagesize=A4)
    width, height = A4
    
    margin = 50
    c_width = width - (margin * 2)
    c_height = (height - (margin * 4)) / 3
    
    for i in range(num_inici, num_final + 1):
        pos_en_pagina = (i - num_inici) % 3
        y_offset = height - margin - (pos_en_pagina + 1) * c_height - (pos_en_pagina * 20)
        
        # Dibuixar Marc del Cartró
        c.setStrokeColor(colors.orange)
        c.setLineWidth(2)
        c.rect(margin, y_offset, c_width, c_height)
        
        # Títol i Número de cartró
        c.setFont("Helvetica-Bold", 10)
        c.drawString(margin + 5, y_offset + c_height + 5, f"BINGO MUSICAL FALLA - Cartró #{i}")
        
        # Lògica de cançons
        dades = generar_cartro_logic()
        
        cell_w = c_width / 9
        cell_h = c_height / 3
        
        for f in range(3):
            for col in range(9):
                x = margin + col * cell_w
                y = y_offset + (2 - f) * cell_h
                
                # Quadrat de la cel·la
                c.setStrokeColor(colors.lightgrey)
                c.setLineWidth(0.5)
                c.rect(x, y, cell_w, cell_h)
                
                contingut = dades[f][col]
                if contingut:
                    # Cel·la amb cançó
                    c.setFont("Helvetica", 6)
                    paraules = contingut.split(" - ")
                    c.drawCentredString(x + cell_w/2, y + cell_h/2 + 2, paraules[0][:15])
                    if len(paraules) > 1:
                        c.setFont("Helvetica-Oblique", 5)
                        c.drawCentredString(x + cell_w/2, y + cell_h/2 - 6, paraules[1][:18])
                else:
                    # Cel·la buida -> Escut + Fons Festiu
                    c.setFillColor(colors.antiquewhite) # Fons festiu suau
                    c.rect(x+1, y+1, cell_w-2, cell_h-2, fill=1, stroke=0)
                    try:
                        c.drawImage("escut.jpg", x+5, y+5, width=cell_w-10, height=cell_h-10, preserveAspectRatio=True, mask='auto')
                    except:
                        pass # Si no troba la imatge, continua
                    c.setFillColor(colors.black)

        if pos_en_pagina == 2 or i == num_final:
            c.showPage()
            
    c.save()

# EXECUTAR LA GENERACIÓ
print("Generant els 3 documents...")
dibuixar_pdfs(1, 100, "Bingo_Musical_1_100.pdf")
dibuixar_pdfs(101, 200, "Bingo_Musical_101_200.pdf")
dibuixar_pdfs(201, 300, "Bingo_Musical_201_300.pdf")
print("Fet! Ja tens els 300 cartrons en 3 arxius.")
