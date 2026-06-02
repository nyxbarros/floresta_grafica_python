from engine.shader import Shader

VERTEX_SHADER = """
#version 400

layout(location = 0) in vec3 in_pos;
layout(location = 1) in vec2 in_uv;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

out vec2 frag_uv;

void main()
{
    frag_uv = in_uv;

    gl_Position =
        projection *
        view *
        model *
        vec4(in_pos,1.0);
}
"""

FRAGMENT_SHADER = """
#version 400

in vec2 frag_uv;

uniform sampler2D texture1;

out vec4 FragColor;

void main()
{
    FragColor =
        texture(texture1, frag_uv);
}
"""

class TexturedShader(Shader):

    def __init__(self):

        super().__init__(
            VERTEX_SHADER,
            FRAGMENT_SHADER
        )