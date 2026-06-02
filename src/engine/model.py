from OpenGL.GL import *

import ctypes
import numpy as np

from src.engine.texture_loader import load_texture
from src.engine.obj_loader_simple import ObjLoaderSimple

import pyrr
import numpy as np
from pyrr import Vector3

class Model:

    def __init__(self, arquivo_obj, arquivo_tex, translation=[0.0, 0.0, 0.0],rotation=[0.0, 0.0, 0.0],scale=[1.0, 1.0, 1.0]):
        self.vao = None
        self.vbo = None
        self.textura = None
        self.num_vertices = 0
        self.set_model_matrix(translation, rotation, scale)
        self.carregar(arquivo_obj,arquivo_tex)

    def carregar(self, arquivo_obj, arquivo_tex):

        buffer, self.num_vertices = (ObjLoaderSimple.load_obj(arquivo_obj))

        buffer = buffer.astype(np.float32)

        # VAO
        self.vao = glGenVertexArrays(1)

        glBindVertexArray(self.vao)

        # VBO
        self.vbo = glGenBuffers(1)

        glBindBuffer(GL_ARRAY_BUFFER,self.vbo)

        glBufferData(GL_ARRAY_BUFFER,buffer.nbytes,buffer,GL_STATIC_DRAW)

        stride = buffer.itemsize * 5

        # posição
        glEnableVertexAttribArray(0)

        glVertexAttribPointer(0,3,GL_FLOAT,GL_FALSE,stride,ctypes.c_void_p(0))

        # UV
        glEnableVertexAttribArray(1)

        glVertexAttribPointer(1,2,GL_FLOAT,GL_FALSE,stride,ctypes.c_void_p(buffer.itemsize * 3))

        glBindBuffer(GL_ARRAY_BUFFER, 0)

        glBindVertexArray(0)

        # textura
        self.textura = glGenTextures(1)

        load_texture(arquivo_tex,self.textura)

    def draw(self, shader):

        shader.set_matrix4("model",self.model_matrix)

        glBindVertexArray(self.vao)

        glBindTexture(GL_TEXTURE_2D,self.textura)

        glDrawArrays(GL_TRIANGLES,0,self.num_vertices)

    def set_model_matrix(self,translation=[0.0, 0.0, 0.0],rotation=[0.0, 0.0, 0.0],scale=[1.0, 1.0, 1.0]):

        # garante Vector3
        translation = Vector3(translation)
        rotation = Vector3(rotation)
        scale = Vector3(scale)

        # ESCALA
        scale_matrix = pyrr.matrix44.create_from_scale(scale)

        # ROTAÇÕES
        rot_x = pyrr.matrix44.create_from_x_rotation(np.radians(rotation.x))

        rot_y = pyrr.matrix44.create_from_y_rotation(np.radians(rotation.y))

        rot_z = pyrr.matrix44.create_from_z_rotation(np.radians(rotation.z))

        # TRANSLAÇÃO
        translation_matrix = pyrr.matrix44.create_from_translation(translation)

        # composição (ordem importa!)
        model = pyrr.matrix44.multiply(rot_x, scale_matrix)
        model = pyrr.matrix44.multiply(rot_y, model)
        model = pyrr.matrix44.multiply(rot_z, model)
        model = pyrr.matrix44.multiply(translation_matrix, model)

        self.model_matrix = model