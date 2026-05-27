from src.engine.model import Model
from pyrr import Vector3
import pyrr
import numpy as np

class Objetos:
    lista_objetos = []

    @staticmethod
    def gerar():

        # CHIBI
        chibi = Model(
            "src/objetos/chibi/chibi.obj",
            "src/objetos/chibi/chibi.png"
        )

        escala = pyrr.matrix44.create_from_scale(
            Vector3([0.4, 0.4, 0.4])
        )

        translacao = (
            pyrr.matrix44.create_from_translation(
                Vector3([-2.0, 0.0, 0.0])
            )
        )

        chibi.model_matrix = (
            pyrr.matrix44.multiply(
                translacao,
                escala
            )
        )

        Objetos.lista_objetos.append(chibi)

        # CAT
        cat = Model(
            "src/objetos/Cat/Cat.obj",
            "src/objetos/Cat/Cat_diffuse.jpg"
        )

        escala = pyrr.matrix44.create_from_scale(
            Vector3([0.12, 0.12, 0.12])
        )

        rot_x = (
            pyrr.matrix44.create_from_x_rotation(
                np.radians(90)
            )
        )

        translacao = (
            pyrr.matrix44.create_from_translation(
                Vector3([15.5, -1.5, 0.0])
            )
        )

        model = pyrr.matrix44.multiply(
            rot_x,
            escala
        )

        model = pyrr.matrix44.multiply(
            translacao,
            model
        )

        cat.model_matrix = model

        Objetos.lista_objetos.append(cat)

        return Objetos.lista_objetos