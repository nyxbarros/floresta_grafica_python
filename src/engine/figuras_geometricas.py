from math import radians, sin, cos
import numpy as np

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

class FiguraGeometricaEquilatera(FiguraGeometrica):
    def __init__(self, quanti_lados, colors, scale : list[float, float, float] | float, translation = [0, 0, 0], rotation = [0, 0, 0]):
        angulo = 360/quanti_lados

        self.coordenadas = []
        if type(scale) == float or type(scale) == int:
            for i in range(quanti_lados):
                coordenada = [
                    [scale*sin(radians(angulo*i)) + translation[0]],
                    [translation[1]],
                    [scale*cos(radians(angulo*i)) + translation[2]],
                    [1]
                ]
                coordenada = FiguraGeometricaEquilatera.rotation_xyz(rotation) @ coordenada
                self.coordenadas += [coordenada[0][0], coordenada[1][0], coordenada[2][0]]

        elif type(scale) == list or type(scale) == tuple:
            for i in range(quanti_lados):
                coordenada = [
                    [scale[0]*sin(radians(angulo*i)) + translation[0]],
                    [translation[1]],
                    [scale[2]*cos(radians(angulo*i)) + translation[2]],
                    [1]
                ]
                coordenada = FiguraGeometricaEquilatera.rotation_xyz(rotation) @ coordenada
                self.coordenadas += [coordenada[0][0], coordenada[1][0], coordenada[2][0]]

        super().__init__(self.coordenadas, colors)

    @staticmethod
    def rotation_x(ang):
        c = cos(radians(ang))
        s = sin(radians(ang))

        return np.array([
            [1, 0,  0, 0],
            [0, c, -s, 0],
            [0, s,  c, 0],
            [0, 0,  0, 1]
        ], dtype=np.float32)

    @staticmethod
    def rotation_y(ang):
        c = cos(radians(ang))
        s = sin(radians(ang))

        return np.array([
            [ c, 0, s, 0],
            [ 0, 1, 0, 0],
            [-s, 0, c, 0],
            [ 0, 0, 0, 1]
        ], dtype=np.float32)

    @staticmethod
    def rotation_z(ang):
        c = cos(radians(ang))
        s = sin(radians(ang))

        return np.array([
            [c, -s, 0, 0],
            [s,  c, 0, 0],
            [0,  0, 1, 0],
            [0,  0, 0, 1]
        ], dtype=np.float32)

    @staticmethod
    def rotation_xyz(coordenadas):
        rx = FiguraGeometricaEquilatera.rotation_x(coordenadas[0])
        ry = FiguraGeometricaEquilatera.rotation_y(coordenadas[1])
        rz = FiguraGeometricaEquilatera.rotation_z(coordenadas[2])

        return rz @ ry @ rx