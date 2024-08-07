from app.vistas import VistaTituloPagina, VistaCatalogo
from app.modelos import Pelicula, Director
from simple_screen import Screen_manager, Input, cls, Print, DIMENSIONS, locate

tit1 = VistaTituloPagina("SIMULADOR DE CAJA")
tit2 = VistaTituloPagina("=================", 2)
p1 = Productos(1, "Manzana", 0.50 + "€", 0, 0.00 + "€")
p2 = Pelicula("Titulo2", "Sinopsis distinta", Director("Isabel Coixet", 2))
p3 = Pelicula("Titulo3", "Sinopsis 3", Director("director 4", 4))
p4 = Pelicula("Titulo4", "Sinopsis cuaggro", Director("El nuevo", 44))

vista_catalogo = VistaCatalogo([p1, p2, p3, p4], 3, 3, 89, 3)

with Screen_manager:
    cls()
    tit1.paint()
    tit2.paint()
    vista_catalogo.paint()

    locate(0, DIMENSIONS.h - 1)
    Input("Codigo del producto o X para terminar compra:")
    Input("Ingrese el numero de unidades:")
    Input()
    Input("¿Nueva compra?: (S/N)")
