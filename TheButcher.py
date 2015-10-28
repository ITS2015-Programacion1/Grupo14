# coding: utf-8
import pilasengine

pilas = pilasengine.iniciar()
fondo = pilas.fondos.Fondo()
fondo.imagen=pilas.imagenes.cargar("fondo_menu.jpg")
        
def jugar():
    pilas.ejemplos.Piezas()
    """Podemos comenzar a jugar desde el menú con el botón Jugar"""

def salir():    
    salir = pilas.terminar()
    
    """Podemos cerrar el juego desde el menú con el botón Cerrar"""
def ayuda():
    """Si pulsamos el botón Ayuda ubicado en el menú se mostrará contenido como los controles, jugabilidad, personajes, etc."""   
pilas.actores.Menu(
        [
            ("Jugar", jugar),
            ("Ayuda", ayuda),
            ("Salir", salir)
        ])

pilas.ejecutar()

