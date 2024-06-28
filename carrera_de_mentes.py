import pygame
from constantes import *
from funciones import *

#Separa set de datos en sub-listas
lista_preguntas = enlistar_datos(lista,"pregunta")
lista_rta_a = enlistar_datos(lista,"a")
lista_rta_b = enlistar_datos(lista,"b")
lista_rta_c = enlistar_datos(lista,"c")
lista_rta_correcta = enlistar_datos(lista,"correcta")
lista_tema = enlistar_datos(lista,"tema")

#Inicializa Pygame y el módulo de sonido
pygame.init()
pygame.mixer.init()

#CONFIGURACIÓN VENTANA e imágenes
icon = pygame.image.load(RUTA_IMAGEN+"icon.jpeg")
pantalla = pygame.display.set_mode(TAMAÑO_PANTALLA)
pygame.display.set_caption("Juego de Mentes")
pygame.display.set_icon(icon)

#Imágenes utilizadas
imagen = pygame.image.load(RUTA_IMAGEN+"imagen.jpg")
imagen = pygame.transform.scale(imagen,(250,250))
corazon = pygame.image.load(RUTA_IMAGEN+"corazon.png")
corazon = pygame.transform.scale(corazon,(40,40))
pantalla_perdio = pygame.image.load(RUTA_IMAGEN+"perdio.png")
pantalla_perdio = pygame.transform.scale(pantalla_perdio,(450,450))
pantalla_gano = pygame.image.load(RUTA_IMAGEN+"ganador.png")
pantalla_gano = pygame.transform.scale(pantalla_gano,(450,450))

#Cargar sonidos
sonido_error = pygame.mixer.Sound(RUTA_SONIDO+"daño.wav")
sonido_perdio = pygame.mixer.Sound(RUTA_SONIDO+"perdio.wav")
sonido_gano = pygame.mixer.Sound(RUTA_SONIDO+"gano.wav")
sonido_correcto = pygame.mixer.Sound(RUTA_SONIDO+"correcto.wav")

#Inicializa variables de juego
correr = True

#Fuentes
fuente = pygame.font.SysFont("Monocraft",20)
fuente_puntaje = pygame.font.SysFont("Monocraft",40)
fuente_equis = pygame.font.SysFont("Monocraft",50)

#Textos
boton_pregunta = fuente.render("Pregunta",True,COLOR_NEGRO)
boton_reinicio = fuente.render("Reiniciar",True,COLOR_NEGRO)
texto_tema = fuente.render("Tema: ",True,COLOR_MORADO)
texto_vida = fuente.render("Vidas: ",True,COLOR_NEGRO)

#Variables de estado del juego
posicion = 0
puntos = 0
vidas = 2
bandera_correcta = False
respondida = False
bandera_perdio = False
bandera_gano = False

#Pregunta y respuestas iniciales
# pregunta = lista_preguntas[posicion]
# respuesta_A = lista_rta_a[posicion]
# respuesta_B = lista_rta_b[posicion]
# respuesta_C = lista_rta_c[posicion]
# correcta = lista_rta_correcta[posicion]
# tema = lista_tema[posicion]

while correr:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            correr = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            click = event.pos
            # print(click)

            if btn_pregunta.collidepoint(click) and not \
                bandera_perdio and not bandera_gano:
                posicion = cambiar_posicion(posicion,lista_preguntas)
                respondida = False
            elif btn_reinicio.collidepoint(click):
                #Reinicia el juego
                puntos = 0
                posicion = 0
                vidas = 2
                respondida = False
                bandera_perdio = False
                bandera_gano = False
                sonido_gano.stop()
            elif not respondida and not \
                bandera_perdio and not bandera_gano:
                if correcta == 'a':
                    if btn_a.collidepoint(click):
                        bandera_correcta = True
                    elif btn_b.collidepoint(click) or btn_c.collidepoint(click):
                        vidas -= 1
                        sonido_error.play()
                elif correcta == 'b':
                    if btn_b.collidepoint(click):
                        bandera_correcta = True
                    elif btn_a.collidepoint(click) or btn_c.collidepoint(click):
                        vidas -= 1
                        sonido_error.play()
                elif correcta == 'c':
                    if btn_c.collidepoint(click):
                        bandera_correcta = True
                    elif btn_a.collidepoint(click) or btn_b.collidepoint(click):
                        vidas -= 1
                        sonido_error.play()

    if bandera_correcta == True and not respondida and bandera_perdio == False:
        puntos += 10
        respondida = True
        sonido_correcto.play()
        bandera_correcta = False

    if vidas == 0 and not bandera_perdio:
        bandera_perdio = True
        sonido_perdio.play()

    if posicion >= len(lista_preguntas) - 1 and respondida and vidas > 0 and not bandera_gano:
        bandera_gano = True
        sonido_gano.play(-1)

    #Actualiza la pregunta y las respuestas
    pregunta = lista_preguntas[posicion]
    respuesta_A = lista_rta_a[posicion]
    respuesta_B = lista_rta_b[posicion]
    respuesta_C = lista_rta_c[posicion]
    correcta = lista_rta_correcta[posicion]
    tema = lista_tema[posicion]

    #RENDER TEXTO(CONVERTIR TEXTO A IMAGEN)
    preguntas = fuente.render(str(pregunta), True, (COLOR_BLANCO))
    respuesta_a = fuente.render(str(respuesta_A), True, (COLOR_BLANCO))
    respuesta_b = fuente.render(str(respuesta_B), True, (COLOR_BLANCO))
    respuesta_c = fuente.render(str(respuesta_C), True, (COLOR_BLANCO))
    puntaje = fuente_puntaje.render(str(puntos),True,COLOR_NEGRO)
    tema = fuente.render(tema,True,COLOR_MORADO)
    
    pantalla.fill(COLOR_PANTALLA)

    #RECTÁNGULOS BOTONES
    btn_pregunta = pygame.draw.rect(pantalla,COLOR_BTN,(POS_PREGUNTA))
    btn_a = pygame.draw.rect(pantalla, COLOR_BTN, (POS_A))
    btn_b = pygame.draw.rect(pantalla, COLOR_BTN, (POS_B))
    btn_c = pygame.draw.rect(pantalla, COLOR_BTN, (POS_C))

    recuadro_tema = pygame.draw.rect(pantalla,COLOR_BTN,(POS_TEMA))

    #DIBUJAR EN PANTALLA
    pantalla.blit(boton_pregunta, (470,153))

    pantalla.blit(preguntas,(200, 410))

    if respondida != True and bandera_perdio != True:
        pantalla.blit(respuesta_a, (200, 480))
        pantalla.blit(respuesta_b, (600, 480))
        pantalla.blit(respuesta_c, (400, 580))

    pantalla.blit(texto_vida,(600,245))

    #corazones
    for i in range(vidas):
        pantalla.blit(corazon, (600 + 50 * i, 280))
    
    pantalla.blit(texto_tema,(80,370))
    pantalla.blit(tema,(150,370))

    pantalla.blit(imagen,(POS_IMAGEN))

    if bandera_perdio == True:
        pantalla.fill(COLOR_LAVANDA)
        pantalla.blit(pantalla_perdio,(80,112))
    elif bandera_gano == True:
        pantalla.fill(COLOR_DORADO)
        pantalla.blit(pantalla_gano,(80,112))

    pantalla.blit(puntaje,(720,150))

    #Boton reinicio
    btn_reinicio = pygame.draw.rect(pantalla,COLOR_BTN,(POS_REINICIO))
    pantalla.blit(boton_reinicio, (470,721))

    pygame.display.flip()

pygame.mixer.quit()
pygame.quit()

