from OpenGL.GL import *


vertices = (
    (1, -1, -1),
    (1, -3, -1),
    (-1, -1, -1),
    (-1, -2, -1),
    (1, -5, -1),
    (1, -1, -1),
    (-5, -1, -1),
    (1, -1, -1),
    (1, -3, -4),
    (-1, -2, -1),
    (1, -1, -1),
    (1, -2, 5),
    (1, -6, -4),
    (-1, -6, -1),
    (1, -2, -1),
)

edges = (
    (6, 1),
    (1, 3),
    (5, 4),
    (2, 1),
    (2, 4),
    (2, 6),
    (6, 1),
    (0, 3),
    (8, 4),
    (6, 1),
    (3, 5),
    (4, 1),
)


def teste():
    glBegin(GL_LINES)

    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])

    glEnd()
