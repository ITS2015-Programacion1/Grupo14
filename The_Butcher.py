# coding: utf-8
import pilasengine

import sys
sys.path.insert(0, "..")
import random

pilas = pilasengine.iniciar()

pilas.actores.Sonido()

class Pudge(pilasengine.actores.Actor):

    def iniciar(self):
        self.imagen = "pudge.png"

    def actualizar(self):
        if pilas.control.izquierda:
            self.x -= 10
            self.espejado = True
        elif pilas.control.derecha:
            self.x += 10
            self.espejado = False

teclas ={
	    pilas.simbolos.a: "Disparar",
	    pilas.simbolos.s: "disparar",
	}

class MiMunicion(pilasengine.actores.Actor):

    def iniciar(self):
        self.imagen = "carne.png"
        self.escala_y = .2
        self.escala_x = .2
        MiMunicion.escala =[2,0,0.1],.1

pilas.actores.vincular(MiMunicion)

pilas.fondos.Espacio()
pudge = Pudge(pilas)
pudge.x = 0
pudge.y = -100
pudge.escalar = 0.5
pudge.aprender(pilas.habilidades.LimitadoABordesDePantalla)

mimunicion=MiMunicion(pilas)


def dispara():
     pudge.disparar()
     return True 

def enemigo_destruido(MiMunicion2, enemigo):
    enemigo.eliminar()
    MiMunicion2.eliminar()

class MiMunicion2(pilasengine.actores.Actor):

     def iniciar(self):
	self.imagen = "gancho.png"
	self.escala_y = .2
	self.escala_x = .2
	MiMunicion2.escala =[2,0,0.1],.1

pilas.actores.vincular(MiMunicion2)

mimunicion2=MiMunicion2(pilas)

mi_control = pilas.control.Control(teclas)
a = pilas.simbolos.a
s = pilas.simbolos.s

pudge.aprender("disparar", municion="MiMunicion2", angulo_salida_disparo = 90)

class Mafioso(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen ="mafia.png"
        self.direccion=-1
        self.rotacion=90
        self.y = 240
        self.x = pilas.azar(-320, 320)
        self.velocidad = pilas.azar(15, 20) / 4.0

    def actualizar(self):
        self.y -= self.velocidad

pilas.actores.vincular(Mafioso)
enemigos=[]
fin_de_juego = False
def crear_enemigo():
    enemigo=pilas.actores.Mafioso()
    enemigo.aprender(pilas.habilidades.PuedeExplotar)
    enemigo.escala=.25
    '''

    tipo_interpolacion=["lineal",
                        "aceleracion_gradual"]
                        
    duracion = 1 +random.random()*4

    pilas.utils.interpolar(enemigo, "x", 0, duracion)
    pilas.utils.interpolar(enemigo, "y", 0, duracion)
    '''
    enemigos.append(enemigo)
    if fin_de_juego:
        return False
    else:
        return True

agregar_enemigo = pilas.tareas.agregar(1, crear_enemigo)

pilas.ejecutar()
