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



    '''
    ANIMAL
    src/objetos/kenney_cube-pets_1.0
    '''
    animal = {

    }

    @classmethod
    def gerar(cls):
        pedras = [
            # src/objetos/kenney_fantasy-town-kit_2.0
            ['src/objetos/kenney_fantasy-town-kit_2.0/OBJ format/rock-small.obj', 'src/objetos/kenney_fantasy-town-kit_2.0/OBJ format/Textures/colormap.png'],
            ['src/objetos/kenney_fantasy-town-kit_2.0/OBJ format/rock-large.obj', 'src/objetos/kenney_fantasy-town-kit_2.0/OBJ format/Textures/colormap.png'],
            ['src/objetos/kenney_fantasy-town-kit_2.0/OBJ format/rock-wide.obj', 'src/objetos/kenney_fantasy-town-kit_2.0/OBJ format/Textures/colormap.png'],

            # src/objetos/kenney_graveyard-kit_5.0
            ['src/objetos/kenney_graveyard-kit_5.0/OBJ format/rocks.obj', 'src/objetos/kenney_graveyard-kit_5.0/OBJ format/Textures/colormap.png'],
            ['src/objetos/kenney_graveyard-kit_5.0/OBJ format/rocks-tall.obj', 'src/objetos/kenney_graveyard-kit_5.0/OBJ format/Textures/colormap.png'],

            # src/objetos/kenney_pirate-kit
            ['src/objetos/kenney_pirate-kit/OBJ format/tower-base.obj', 'src/objetos/kenney_pirate-kit/OBJ format/Textures/colormap.png'],
            ['src/objetos/kenney_pirate-kit/OBJ format/tower-base-door.obj', 'src/objetos/kenney_pirate-kit/OBJ format/Textures/colormap.png'],
            ['src/objetos/kenney_pirate-kit/OBJ format/rocks-a.obj', 'src/objetos/kenney_pirate-kit/OBJ format/Textures/colormap.png'],
            ['src/objetos/kenney_pirate-kit/OBJ format/rocks-b.obj', 'src/objetos/kenney_pirate-kit/OBJ format/Textures/colormap.png'],
            ['src/objetos/kenney_pirate-kit/OBJ format/rocks-c.obj', 'src/objetos/kenney_pirate-kit/OBJ format/Textures/colormap.png'],
            ['src/objetos/kenney_pirate-kit/OBJ format/rocks-sand-a.obj', 'src/objetos/kenney_pirate-kit/OBJ format/Textures/colormap.png'],
            ['src/objetos/kenney_pirate-kit/OBJ format/rocks-sand-c.obj', 'src/objetos/kenney_pirate-kit/OBJ format/Textures/colormap.png'],
            ['src/objetos/kenney_pirate-kit/OBJ format/rocks-sand-b.obj', 'src/objetos/kenney_pirate-kit/OBJ format/Textures/colormap.png'],

            # src/objetos/kenney_platformer-kit
            ['src/objetos/kenney_platformer-kit/OBJ format/rocks.obj', 'src/objetos/kenney_platformer-kit/OBJ format/Textures/colormap.png'],

            # src/objetos/kenney_survival-kit
            ['src/objetos/kenney_survival-kit/OBJ format/rock-sand-c.obj', 'src/objetos/kenney_survival-kit/OBJ format/Textures/colormap.png'],
            ['src/objetos/kenney_survival-kit/OBJ format/rock-a.obj', 'src/objetos/kenney_survival-kit/OBJ format/Textures/colormap.png'],
            ['src/objetos/kenney_survival-kit/OBJ format/rock-sand-a.obj', 'src/objetos/kenney_survival-kit/OBJ format/Textures/colormap.png'],
            ['src/objetos/kenney_survival-kit/OBJ format/rock-b.obj', 'src/objetos/kenney_survival-kit/OBJ format/Textures/colormap.png'],
            ['src/objetos/kenney_survival-kit/OBJ format/rock-sand-b.obj', 'src/objetos/kenney_survival-kit/OBJ format/Textures/colormap.png'],
            ['src/objetos/kenney_survival-kit/OBJ format/rock-c.obj', 'src/objetos/kenney_survival-kit/OBJ format/Textures/colormap.png'],
            ['src/objetos/kenney_survival-kit/OBJ format/resource-stone.obj', 'src/objetos/kenney_survival-kit/OBJ format/Textures/colormap.png'],
        ]

        arvore = [
            # src/objetos/kenney_fantasy-town-kit_2.0
            ['src/objetos/kenney_fantasy-town-kit_2.0/OBJ format/tree.obj', 'src/objetos/kenney_fantasy-town-kit_2.0/OBJ format/Textures/colormap.png'],
            ['src/objetos/kenney_fantasy-town-kit_2.0/OBJ format/tree-high.obj', 'src/objetos/kenney_fantasy-town-kit_2.0/OBJ format/Textures/colormap.png'],

            # src/objetos/kenney_graveyard-kit_5.0
            ['src/objetos/kenney_graveyard-kit_5.0/OBJ format/pine.obj', 'src/objetos/kenney_graveyard-kit_5.0/OBJ format/Textures/colormap.png'],
            ['src/objetos/kenney_graveyard-kit_5.0/OBJ format/pine-fall.obj', 'src/objetos/kenney_graveyard-kit_5.0/OBJ format/Textures/colormap.png'],
        ]

        graminha = [
            # src/objetos/kenney_pirate-kit
            ['src/objetos/kenney_pirate-kit/OBJ format/grass.obj', 'src/objetos/kenney_pirate-kit/OBJ format/Textures/colormap.png'],
            ['src/objetos/kenney_pirate-kit/OBJ format/grass-patch.obj', 'src/objetos/kenney_pirate-kit/OBJ format/Textures/colormap.png'],
            ['src/objetos/kenney_pirate-kit/OBJ format/grass-plant.obj', 'src/objetos/kenney_pirate-kit/OBJ format/Textures/colormap.png'],

            # src/objetos/kenney_survival-kit
            ['src/objetos/kenney_survival-kit/OBJ format/grass-large.obj', 'src/objetos/kenney_survival-kit/OBJ format/Textures/colormap.png'],
            ['src/objetos/kenney_survival-kit/OBJ format/grass.obj', 'src/objetos/kenney_survival-kit/OBJ format/Textures/colormap.png'],
        ]

        caminho = [
            # src/objetos/kenney_graveyard-kit_5.0
            ['src/objetos/kenney_graveyard-kit_5.0/OBJ format/road.obj', 'src/objetos/kenney_graveyard-kit_5.0/OBJ format/Textures/colormap.png'],

            # src/objetos/kenney_platformer-kit
            ['src/objetos/kenney_platformer-kit/OBJ format/stones.obj', 'src/objetos/kenney_platformer-kit/OBJ format/Textures/colormap.png'],
        ]

        morrinho = [
            # src/objetos/kenney_platformer-kit
            ['block-grass-large-tall.obj', 'src/objetos/kenney_platformer-kit/OBJ format/Textures/colormap.png'],
            ['block-grass-overhang-large-tall.obj', 'src/objetos/kenney_platformer-kit/OBJ format/Textures/colormap.png'],
            ['block-grass-overhang-low-large.obj', 'src/objetos/kenney_platformer-kit/OBJ format/Textures/colormap.png'],

            # src/objetos/kenney_survival-kit
            ['src/objetos/kenney_survival-kit/OBJ format/rock-flat-grass.obj', 'src/objetos/kenney_survival-kit/OBJ format/Textures/colormap.png'],
            ['src/objetos/kenney_survival-kit/OBJ format/rock-flat.obj', 'src/objetos/kenney_survival-kit/OBJ format/Textures/colormap.png'],
        ]

        tronco = [
            # src/objetos/kenney_graveyard-kit_5.0
            ['src/objetos/kenney_graveyard-kit_5.0/OBJ format/trunk.obj', 'src/objetos/kenney_graveyard-kit_5.0/OBJ format/Textures/colormap.png'],
            ['src/objetos/kenney_graveyard-kit_5.0/OBJ format/trunk-round.obj', 'src/objetos/kenney_graveyard-kit_5.0/OBJ format/Textures/colormap.png'],

            # src/objetos/kenney_survival-kit
            ['src/objetos/kenney_survival-kit/OBJ format/tree-trunk.obj','src/objetos/kenney_survival-kit/OBJ format/Textures/colormap.png'],
            ['src/objetos/kenney_survival-kit/OBJ format/tree-log-small.obj','src/objetos/kenney_survival-kit/OBJ format/Textures/colormap.png'],
            ['src/objetos/kenney_survival-kit/OBJ format/tree-log.obj','src/objetos/kenney_survival-kit/OBJ format/Textures/colormap.png'],
        ]
        cls.__lista_objetos = [
            FiguraGeometricaEquilatera(30, [0.0, 0.25, 0.0], 25), # base
            Model(
                *tronco[0],
                translation=[-10,0,0]
            ),
            Model(
                "src/objetos/kenney_fantasy-town-kit_2.0/OBJ format/tree-high-round.obj",
                'src/objetos/kenney_fantasy-town-kit_2.0/OBJ format/Textures/colormap.png',
                translation=[10,0,0]
            ),
            Model(
                "src/objetos/kenney_fantasy-town-kit_2.0/OBJ format/tree-high.obj",
                'src/objetos/kenney_fantasy-town-kit_2.0/OBJ format/Textures/colormap.png'
            ),
        ]