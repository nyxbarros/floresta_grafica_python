from engine.figuras_geometricas import FiguraGeometrica, FiguraGeometricaEquilatera
from engine.model import Model

class Objetos:
    __lista_objetos = []

    @classmethod
    def set_lista_objetos(cls):
        if cls.__lista_objetos == []:
            cls.gerar()
        return cls.__lista_objetos

    @classmethod
    def gerar(cls):
        pedra = [
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
            ['src/objetos/kenney_platformer-kit/OBJ format/block-grass-large-tall.obj', 'src/objetos/kenney_platformer-kit/OBJ format/Textures/colormap.png'],
            ['src/objetos/kenney_platformer-kit/OBJ format/block-grass-overhang-large-tall.obj', 'src/objetos/kenney_platformer-kit/OBJ format/Textures/colormap.png'],
            ['src/objetos/kenney_platformer-kit/OBJ format/block-grass-overhang-low-large.obj', 'src/objetos/kenney_platformer-kit/OBJ format/Textures/colormap.png'],

            # src/objetos/kenney_survival-kit
            ['src/objetos/kenney_survival-kit/OBJ format/rock-flat-grass.obj', 'src/objetos/kenney_survival-kit/OBJ format/Textures/colormap.png'],
            ['src/objetos/kenney_survival-kit/OBJ format/rock-flat.obj', 'src/objetos/kenney_survival-kit/OBJ format/Textures/colormap.png'],
        ]

        tronco = [
            # src/objetos/kenney_graveyard-kit_5.0
            ['src/objetos/kenney_graveyard-kit_5.0/OBJ format/trunk.obj', 'src/objetos/kenney_graveyard-kit_5.0/OBJ format/Textures/colormap.png'],
            ['src/objetos/kenney_graveyard-kit_5.0/OBJ format/trunk-long.obj', 'src/objetos/kenney_graveyard-kit_5.0/OBJ format/Textures/colormap.png'],

            # src/objetos/kenney_survival-kit
            ['src/objetos/kenney_survival-kit/OBJ format/tree-trunk.obj','src/objetos/kenney_survival-kit/OBJ format/Textures/colormap.png'],
            ['src/objetos/kenney_survival-kit/OBJ format/tree-log-small.obj','src/objetos/kenney_survival-kit/OBJ format/Textures/colormap.png'],
            ['src/objetos/kenney_survival-kit/OBJ format/tree-log.obj','src/objetos/kenney_survival-kit/OBJ format/Textures/colormap.png'],
        ]
        cls.__lista_objetos = [
            FiguraGeometricaEquilatera(50, [0.0, 0.25, 0.0], 35), # base
            Model( # tronco 1
                *tronco[3],
                scale=[10,10,10],
                rotation=[0,30,0]
            ),
            Model( # tronco 2
                *tronco[3],
                scale=[15,10,10],
                rotation=[30,-30,0],
                translation=[0,0.2,-0.2]
            ),

            Model( # morrinho 1
                *morrinho[3],
                translation=[-0.75,0,-0.75],
                scale=[20,10,20],
                rotation=[0,0,0]
            ),
            Model( # arvore 1.1
                *arvore[2],
                scale=[7,7,7],
                translation=[-3,0.2,-2.5],
            ),
            Model( # arvore 1.2
                *arvore[2],
                scale=[5,5,5],
                translation=[-3,0.3,-4],
            ),
            Model( # arvore 1.3
                *arvore[3],
                scale=[3,3,3],
                translation=[-5.5,0.4,-4.5],
            ),

            Model( # morro 2.1
                *morrinho[1],
                translation=[0,0,-2],
                scale=[12,5,12],
                rotation=[0,60,0]
            ),
            Model( # morro 2.2
                *morrinho[1],
                translation=[0,1,-3],
                scale=[9,7,9],
                rotation=[0,60,0]
            ),
            Model( # morro 2.3
                *morrinho[1],
                translation=[-1.2,3,-6],
                scale=[5,6,5],
                rotation=[0,60,0]
            ),
            Model( # graminha 2.1.1.1
                *graminha[1],
                translation=[10,10,-10],
            ),
            Model( # graminha 2.1.1.2
                *graminha[1],
                translation=[12,10,-10],
            ),
            Model( # graminha 2.1.2.3
                *graminha[1],
                translation=[20,10,0],
            ),
            Model( # graminha 2.1.2.1
                *graminha[1],
                translation=[18,10,1],
            ),
            Model( # graminha 2.1.2.2
                *graminha[1],
                translation=[17,10,-1],
            ),
            Model( # graminha 2.1.3.1
                *graminha[1],
                translation=[30,10,-5],
            ),
            Model( # pedra 2.1.1.1
                *pedra[1],
                translation=[25,10,-3],
            ),
            Model( # pedra 2.1.2.1
                *pedra[1],
                translation=[15,10,-3],
            ),
            Model( # pedra 2.1.2.2
                *pedra[1],
                scale=[0.5,0.5,0.5],
                translation=[30,20,-3],
            ),
            Model( # caminho 2.1.
                *caminho[1],
                scale=[7,7,7],
                translation=[1,-1.7,-0.3],
                rotation=[0,-30,-90],
            ),
            Model( # caminho 2.1.
                *caminho[1],
                scale=[7,7,7],
                translation=[2.2,1.25,4],
                rotation=[0,-120,-90],
            ),
            Model( # graminha 2.2.1.1
                *graminha[1],
                translation=[17,21.3,-10],
            ),
            Model( # graminha 2.2.2.1
                *graminha[1],
                translation=[17,21.3,-7],
            ),
            Model( # graminha 2.2.2.2
                *graminha[1],
                translation=[25,21.3,-5],
            ),
            Model( # pedra 2.2.1.1
                *pedra[1],
                translation=[22,21.3,-3],
            ),

            Model( # morro 3.1
                *morrinho[1],
                translation=[0,0,-2.3],
                scale=[9,7,10],
                rotation=[0,-150,0]
            ),
            Model( # morro 3.2
                *morrinho[1],
                translation=[-0,2,-5],
                scale=[5,6,5],
                rotation=[0,-150,0]
            ),
            Model( # graminha 3.1
                *graminha[1],
                translation=[-4,14,22],
            ),
            Model( # graminha 3.2
                *graminha[1],
                translation=[-10,14,12],
            ),
            Model( # pedra 3.1
                *pedra[1],
                translation=[-8.5,14,25],
            ),
            Model( # caminho 2.1.
                *caminho[1],
                scale=[7,7,7],
                translation=[2.2,1.25,4],
                rotation=[0,-120,-90],
            ),
        ]