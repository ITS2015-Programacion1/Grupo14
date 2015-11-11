# coding: utf-8
import pilasengine

import sys
sys.path.insert(0, "..")

pilas = pilasengine.iniciar()

class Pudge(pilasengine.actores.Actor):

    def iniciar(self):
        self.imagen = "pudge.png"

    def actualizar(self):
        if pilas.control.izquierda:
            self.x -= 5
            self.espejado = True
        elif pilas.control.derecha:
            self.x += 5
            self.espejado = False

pilas.fondos.Selva()
pudge = Pudge(pilas)
pudge.x = 0
pudge.y = -100
pudge.escalar = 0.5
pilas.ejecutar()
