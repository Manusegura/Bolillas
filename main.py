import pygame as pg

#inicializar todos los modulos de pygame
#pantallas, sonidos, teclados etc
pg.init()

#crear pantalla o surface
pantalla_principal = pg.display.set_mode( (800,600) )#ventana y tamañño de ventana
pg.display.set_caption('Bolillas Rebotando')#Titulo de la ventana

game_over = False
x = 400
y = 300
vx = 1
vy = 1

while not game_over:# bucle para ejecutar los fotogramas para el repintando de pantalla

    for eventos in pg.event.get():#captura todos los eventos de pygame en forma de lista
         print(eventos)
         if eventos.type == pg.QUIT:
            game_over = True

    pantalla_principal.fill( (37, 150, 190) ) #asignar color a la pantalla
    x += vx
    y += vy
    if x >= 800 or x == 0:
     vx *= -1
    if y >= 600 or y == 0:
     vy *= -1


        
                # surface o pantalla, color ,medidas posicion(400,300), medidas rectanculo 40,20)
    pg.draw.rect(pantalla_principal,(234,182,118),(x,y,40,20))
    pg.display.flip()# apunta todo a la pantalla, todo lo que hagas, antes de esto si no no sale.

    

pg.quit()

#Crear clase y poner 20 bolitas
