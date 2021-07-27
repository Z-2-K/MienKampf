from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

#Todo bien #La textura 'brazo' no carga
pasto = load_texture('textures/pasto.jpg')
piedra = load_texture('textures/piedra.jpg')
tierra = load_texture('textures/tierra.jpg')
ladrillo = load_texture('textures/ladrillo.jpg')
bedrock = load_texture('textures/bedrock.png')
cielo = load_texture('textures/cielo.jpg')
brazo = load_texture('textures/brazo.jpg')

tomado = 1

#todo bien #agregar 5
def update():
    global tomado

    if held_keys['1']: tomado = 1
    if held_keys['2']: tomado = 2
    if held_keys['3']: tomado = 3
    if held_keys['4']: tomado = 4

#Todo bien #agregar bedrock
class Voxel(Button):
    def __init__(self, position = (0,0,0), texture = bedrock):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 0.5,
            texture = texture,
            color = color.color(0,0,random.uniform(0.9,1)))
    def input(self,Key):
        if self.hovered:
            if Key == 'right mouse down':
                if tomado == 1: voxel = Voxel(position = self.position + mouse.normal, texture = pasto)
                if tomado == 2: voxel = Voxel(position = self.position + mouse.normal, texture = tierra)
                if tomado == 3: voxel = Voxel(position = self.position + mouse.normal, texture = piedra)
                if tomado == 4: voxel = Voxel(position = self.position + mouse.normal, texture = ladrillo)
                if tomado == 5: voxel = Voxel(position = self.position + mouse.normal, texture = bedrock)

            if Key == 'left mouse down':
                destroy(self)

#Todo bien #Pero debe acomodarse el cielo
class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = cielo,
            scale = 150,
            double_sided = True
        )

#No funciona
class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'textures/brazo',
            texture = brazo,
            scale = 0.2
            )

for z in range(30):
    for x in range(30):
        voxel = Voxel(position = (x,0,z))

Player = FirstPersonController()

#Le falta arreglar los bordes
sky = Sky()

#Inutil
hand = Hand()

app.run()

#troticamente todo funciona perfectamente...