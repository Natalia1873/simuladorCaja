from simple_screen import locate, DIMENSIONS, Input

class VistaTituloPagina:
    def __init__(self, texto: str, y: int = 0):
        self.texto = texto
        self.y = y

    def paint(self):
        x = (DIMENSIONS.w - len(self.texto)) // 2
        locate(x, self.y, self.texto)

class VistaCatalogo:
    def __init__(self, productos, x:int, y:int, w:int, num_filas:int):
        self.productos = productos
        self.x = x
        self.y = y
        self.w = w
        self.num_filas = num_filas

    def paint(self):
        locate(self.x, self.y, "Codigo")
        locate(self.x + 15, self.y, "|Producto")
        locate(self.x + 30, self.y, "|Precio")
        locate(self.x + 45, self.y, "|Unidades")
        locate(self.x + 60, self.y, "|Total")

        locate(self.x, self.y + 1, "---------------+--------------+--------------------------------------------------")

        for contador, product in enumerate(self.productos):
            locate(self.x, self.y + 2 + contador, product.codigo)
            locate(self.x + 15, self.y + 2 + contador, f"|{product.producto}")
            locate(self.x + 30, self.y + 2 + contador, f"|{product.precio}")
            locate(self.x + 45, self.y + 2 + contador, f"|{product.unidades}")
            locate(self.x + 60, self.y + 2 + contador, f"|{product.total}")

        locate(self.x, self.y + 3 + contador)
        Input("Pulsa Enter para continuar")


        