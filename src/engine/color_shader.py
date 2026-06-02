from engine.shader import Shader

VERTEX_SHADER = """
#version 400

layout(location = 0) in vec3 in_pos;
layout(location = 1) in vec3 in_color;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

out vec3 frag_color;

void main()
{
    frag_color = in_color;

    gl_Position =
        projection *
        view *
        model *
        vec4(in_pos,1.0);
}
"""

FRAGMENT_SHADER = """
#version 400

in vec3 frag_color;

out vec4 FragColor;

void main()
{
    FragColor = vec4(
        frag_color,
        1.0
    );
}
"""

class ColorShader(Shader):

    def __init__(self):

        super().__init__(
            VERTEX_SHADER,
            FRAGMENT_SHADER
        )