import glfw

from OpenGL.GL import *

import pyrr

from engine.camera import Camera
from engine.color_shader import ColorShader

from engine.shader import Shader
from engine.shape import Shape
from engine.textured_shader import TexturedShader

from objetos.objetos import Objetos


class Application:

    def __init__(self):
        self.shader_textura = None
        self.shader_cor = None
        self.width = 800
        self.height = 600

        self.window = None

        self.camera = Camera()

        self.shader = None

        self.first_mouse = True

        self.lastX = self.width / 2
        self.lastY = self.height / 2

    # ======================================================
    # CALLBACKS
    # ======================================================

    def resize_callback(self, window, w, h):

        self.width = w
        self.height = h

        glViewport(0, 0, w, h)

    def key_callback(self,window,key,scancode,action,mods):
        if (key == glfw.KEY_ESCAPE and action == glfw.PRESS):

            glfw.set_window_should_close(window,True)

    def mouse_callback(self,window,xpos,ypos):

        if self.first_mouse:

            self.lastX = xpos
            self.lastY = ypos

            self.first_mouse = False

        xoffset = xpos - self.lastX

        yoffset = self.lastY - ypos

        self.lastX = xpos
        self.lastY = ypos

        self.camera.process_mouse_movement(xoffset,yoffset)

    # ======================================================
    # OPENGL
    # ======================================================

    def init_opengl(self):

        if not glfw.init():
            raise RuntimeError("Erro GLFW")

        self.window = glfw.create_window(self.width,self.height,"OpenGL Moderno",None,None)

        glfw.make_context_current(self.window)

        glfw.set_window_size_callback(self.window,self.resize_callback)

        glfw.set_key_callback(self.window,self.key_callback)

        glfw.set_cursor_pos_callback(self.window,self.mouse_callback)

        glfw.set_input_mode(self.window,glfw.CURSOR,glfw.CURSOR_DISABLED)

        glEnable(GL_DEPTH_TEST)

        glDisable(GL_CULL_FACE)

    # ======================================================
    # SHADER
    # ======================================================

    def init_shader(self):
        self.shader_textura = TexturedShader()
        self.shader_cor = ColorShader()

    # ======================================================
    # INPUT
    # ======================================================

    def process_input(self, vel):

        if glfw.get_key(self.window,glfw.KEY_W) == glfw.PRESS:
            self.camera.process_keyboard("FORWARD",vel)

        if glfw.get_key(self.window,glfw.KEY_S) == glfw.PRESS:
            self.camera.process_keyboard("BACKWARD",vel)

        if glfw.get_key(self.window,glfw.KEY_A) == glfw.PRESS:
            self.camera.process_keyboard("LEFT",vel)

        if glfw.get_key(self.window,glfw.KEY_D) == glfw.PRESS:
            self.camera.process_keyboard("RIGHT",vel)

    # ======================================================
    # RENDER
    # ======================================================

    def render(self):

        glClearColor(0.1, 0.1, 0.1, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        view = self.camera.get_view_matrix()

        projection = pyrr.matrix44.create_perspective_projection_matrix(
            45.0,
            self.width / self.height,
            0.1,
            100.0
        )

        # Configura shader de textura
        self.shader_textura.use()
        self.shader_textura.set_matrix4("view", view)
        self.shader_textura.set_matrix4("projection", projection)

        # Configura shader de cor
        self.shader_cor.use()
        self.shader_cor.set_matrix4("view", view)
        self.shader_cor.set_matrix4("projection", projection)

        for obj in Objetos.set_lista_objetos():

            if isinstance(obj, Shape):
                self.shader_cor.use()
                obj.draw(self.shader_cor)

            else:
                self.shader_textura.use()
                obj.draw(self.shader_textura)

    # ======================================================
    # LOOP
    # ======================================================

    def run(self):

        self.init_opengl()

        self.init_shader()

        last_time = glfw.get_time()

        base_speed = 10.0

        while not glfw.window_should_close(self.window):

            current = glfw.get_time()

            delta = current - last_time

            last_time = current

            vel = base_speed * delta

            self.process_input(vel)

            self.render()

            glfw.swap_buffers(self.window)

            glfw.poll_events()

        glfw.terminate()