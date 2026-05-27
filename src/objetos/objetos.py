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
            )
        ]