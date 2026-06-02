from engine.figuras_geometricas import FiguraGeometrica, FiguraGeometricaEquilatera
from engine.shape import Shape
from src.engine.model import Model

class Objetos:
    __lista_objetos = []

    @classmethod
    def set_lista_objetos(cls):
        if cls.__lista_objetos == []:
            cls.gerar()
        return cls.__lista_objetos

    @classmethod
    def gerar(cls):
        cls.__lista_objetos = [
            FiguraGeometricaEquilatera(30, [0.0, 0.25, 0.0], 15), # base
            Model( # CHIBI
                "src/objetos/chibi/chibi.obj",
                "src/objetos/chibi/chibi.png",
                translation = [-2.0, 0.0, 0.0],
                scale = [0.4, 0.4, 0.4]
            ),
            Model( # GATO
                "src/objetos/Cat/Cat.obj",
                "src/objetos/Cat/Cat_diffuse.jpg",
                scale=[0.12, 0.12, 0.12],
                rotation=[90, 0, 0],
                translation=[15.5, -1.5, 0.0]
            ),
            FiguraGeometrica(
                [
                    -0.5,  0.5, 0.0,  # v0
                    0.5,  0.5, 0.0,  # v1
                    0.5, -0.5, 0.0,   # v3
                    -0.5, -0.5, 0.0  # v2
                ],
                [1.0, 0.0, 0.0]
            ),
        ]