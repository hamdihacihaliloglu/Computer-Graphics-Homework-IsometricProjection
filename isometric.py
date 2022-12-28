import pygame as pg
from pygame.locals import *
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *


kenarlar = ((0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,9),(7,8),(8,9),(3,0),(7,4),(8,2),(6,1),(5,0),(7,9))
x_cisim_nokta =[[0,0,0,1],[1,0,0,1],[1,0,1,1],[0,0,1,1],[0,1,1,1],[0,1,0,1],[1,1,0,1],[0.5,1,1,1],[1,0.5,1,1],[1,1,0.5,1]]

eksen_nokta = [[0,0,0,1],[2.5,0,0,1],[0,0,0,1],[0,2.5,0,1],[0,0,0,1],[0,0,2.5,1]]
eksenler=((0,1),(2,3),(4,5))


izometrik_iz  =[[0.707,-0.408,0,0],[0,0.816,0,0],[-0.707,-0.408,0,0],[0,0,0,1]]

def izometrikHesapla():
     global XYeni
     XYeni = [[] for _ in range(10)]
     for i in range(10):
        for j in range(4):     
            toplam = 0
            for k in range(4):   
               toplam += x_cisim_nokta[i][k] * izometrik_iz[k][j]    
            XYeni[i].append(toplam) 
     XYeni = np.array(XYeni, dtype=np.float32) 

def koordinatHesapla():
     global gecici_eksen
     gecici_eksen = [[] for _ in range(6)]
     for i in range(6):
        for j in range(4):     
            toplam = 0
            for k in range(4):   
               toplam += eksen_nokta[i][k] * izometrik_iz[k][j]    
            gecici_eksen[i].append(toplam) 
     gecici_eksen = np.array(gecici_eksen, dtype=np.float32) 

def izometrikCiz():     
     glBegin(GL_LINES)
     for kenar in kenarlar:
        for i in kenar:
            glVertex3f(XYeni[i][0],XYeni[i][1],XYeni[i][2])
     glEnd()

def eksenCiz():
     glBegin(GL_LINES)
     for eksen in eksenler:
        for i in eksen:
            glVertex3f(gecici_eksen[i][0],gecici_eksen[i][1],gecici_eksen[i][2])
     glEnd()

def main():
    pg.init()
    display = (800, 600)
    pg.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)
    izometrikHesapla()
    koordinatHesapla()
   
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        eksenCiz()
        izometrikCiz()
        pg.display.flip()
        pg.time.wait(10)
if __name__ == "__main__":
    main()
