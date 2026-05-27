from OpenGL.GL import *
import OpenGL.GL.shaders


class Shader:

    def __init__(self, vertex_src, fragment_src):

        self.program = OpenGL.GL.shaders.compileProgram(

            OpenGL.GL.shaders.compileShader(
                vertex_src,
                GL_VERTEX_SHADER
            ),

            OpenGL.GL.shaders.compileShader(
                fragment_src,
                GL_FRAGMENT_SHADER
            )
        )

    def use(self):

        glUseProgram(self.program)

    def set_matrix4(self, name, matrix):

        location = glGetUniformLocation(
            self.program,
            name
        )

        glUniformMatrix4fv(
            location,
            1,
            GL_FALSE,
            matrix
        )