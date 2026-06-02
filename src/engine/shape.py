from OpenGL.GL import *
import ctypes
import numpy as np
import pyrr

class Shape:

    def __init__(self, vertices, colors):

        self.model_matrix = pyrr.matrix44.create_identity(
            dtype='float32'
        )

        self.num_vertices = len(vertices) // 3

        buffer = []

        for i in range(self.num_vertices):

            # posição
            buffer.extend(vertices[i*3:i*3+3])

            # cor
            buffer.extend(colors)

        buffer = np.array(buffer, dtype=np.float32)

        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)

        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)

        glBufferData(
            GL_ARRAY_BUFFER,
            buffer.nbytes,
            buffer,
            GL_STATIC_DRAW
        )

        stride = 6 * 4

        # posição
        glVertexAttribPointer(
            0,
            3,
            GL_FLOAT,
            GL_FALSE,
            stride,
            ctypes.c_void_p(0)
        )
        glEnableVertexAttribArray(0)

        # cor
        glVertexAttribPointer(
            1,
            3,
            GL_FLOAT,
            GL_FALSE,
            stride,
            ctypes.c_void_p(12)
        )
        glEnableVertexAttribArray(1)

    def draw(self, shader):

        shader.set_matrix4(
            "model",
            self.model_matrix
        )

        glBindVertexArray(self.vao)

        glDrawArrays(
            GL_TRIANGLES,
            0,
            self.num_vertices
        )

