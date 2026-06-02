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

    def __init__(self, quanti_lados, colors, scale, translation=[0,0,0], rotation=[0,0,0]):
        if type(scale) == int or type(scale) == float:
            scale = [scale, 0, scale]
        else:
            scale = [scale[0]/2, scale[1]/2, scale[2]/2]

        angulo = 360 / quanti_lados

        R = FiguraGeometricaEquilatera.rotation_xyz(rotation)

        top = []
        bottom = []

        # -------------------------
        # gerar pontos
        # -------------------------

        for i in range(quanti_lados):

            x = scale[0] * sin(radians(angulo*i)) + translation[0]
            z = scale[2] * cos(radians(angulo*i)) + translation[2]

            # topo
            v_top = np.array([x, scale[1]/2 + translation[1], z, 1], dtype=np.float32)
            v_top = R @ v_top
            top.append(v_top[:3])

            # base
            v_bot = np.array([x, -scale[1]/2 + translation[1], z, 1], dtype=np.float32)
            v_bot = R @ v_bot
            bottom.append(v_bot[:3])

        self.coordenadas = []

        if type(scale) == int or type(scale) == float:
            # -------------------------
            # face
            # -------------------------

            for i in range(quanti_lados):
                self.coordenadas += top[i].tolist()

        else:
            # -------------------------
            # topo + base
            # -------------------------

            for i in range(quanti_lados):
                self.coordenadas += top[i].tolist()
                self.coordenadas += bottom[i].tolist()

            # -------------------------
            # laterais (FACES)
            # -------------------------

            for i in range(quanti_lados):
                next_i = (i + 1) % quanti_lados

                # triângulo 1
                self.coordenadas += top[i].tolist()
                self.coordenadas += top[next_i].tolist()
                self.coordenadas += bottom[next_i].tolist()

                # triângulo 2
                self.coordenadas += top[i].tolist()
                self.coordenadas += bottom[next_i].tolist()
                self.coordenadas += bottom[i].tolist()

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