from engine.shape import Shape

class FiguraGeometrica(Shape):
    def __init__(self, coordenadas, colors):
        self.pontos = []
        for i in range(0, len(coordenadas), 3):
            self.pontos.append([coordenadas[i], coordenadas[i+1], coordenadas[i+2]])

        self.mapeamento_triangulos = []
        for i in range(1, len(self.pontos)-1):
            self.mapeamento_triangulos += self.pontos[0] + self.pontos[i] + self.pontos[i+1]

        super().__init__(self.mapeamento_triangulos,colors)

class FiguraGeometricaEquilatera(Shape):