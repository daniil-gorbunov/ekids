from sfml import sf
from round_robin import RoundRobin
from entity import Entity
from enemy import Enemy
from player import Player
from parallaxe_bg import ParallaxeBackground
from util import rect_intersect
import params
import time

RES_WIDTH = 480
RES_HEIGHT = 720
WINDOW_NAME = 'Game'
FRAME_POOL_SIZE = 300

## ЗАГРУЗКА ТЕКСТУР
nebula_texture = sf.Texture.from_file('asset/nebula1.png')
px_stars1_texture = sf.Texture.from_file('asset/stars_bg/spr_stars011.png')
px_stars2_texture = sf.Texture.from_file('asset/stars_bg/spr_stars021.png')
ship_on_texture = sf.Texture.from_file('asset/ship_on.png')
ship_off_texture = sf.Texture.from_file('asset/ship_off.png')
ufo_texture = sf.Texture.from_file('asset/ufo.png')
shell_texture = sf.Texture.from_file('asset/shell.png')
## -----

background = ParallaxeBackground([
  nebula_texture,
  px_stars1_texture,
  px_stars2_texture
], RES_WIDTH)

window = sf.RenderWindow(sf.VideoMode(RES_WIDTH, RES_HEIGHT), WINDOW_NAME)

frames_time = RoundRobin(FRAME_POOL_SIZE, init=0)

objects = []

bars = []
bar_width = RES_WIDTH / FRAME_POOL_SIZE
y_base_pos = RES_HEIGHT
for i in range(FRAME_POOL_SIZE):
  bar = sf.RectangleShape((bar_width, 2))
  bar.fill_color = sf.Color(255, 0, 0, 127)
  bar.position = (i * bar_width, 0)
  bars.append(bar)

clock = sf.Clock()

player = Player(ship_off_texture)
player.shell_texture = shell_texture
player.active_texture = ship_on_texture
player.sprite.position = (RES_WIDTH / 2, RES_HEIGHT / 2)
objects.append(player)

px_shift = 0
px_speed = -0.0013
dt = 0


def place_enemy(pos):
  ufo1 = Enemy()
  ufo1.scale_factor = 0.5
  ufo1.setSprite(ufo_texture)
  ufo1.sprite.position = pos
  objects.append(ufo1)


place_enemy((100, 100))
place_enemy((300, 100))


while window.is_open:
  # CLOCK
  if clock.elapsed_time.microseconds < 2500:
    time.sleep(0.00005)
    continue

  # EVENTS  
  frames_time.add(dt)
  for event in window.events:
      if event == sf.Event.CLOSED:
          window.close()

  # INPUT
  if sf.Keyboard.is_key_pressed(sf.Keyboard.R):
    place_enemy((100, 100))
    place_enemy((300, 100))
    player.sprite.position = (RES_WIDTH / 2, RES_HEIGHT / 2)

  if sf.Keyboard.is_key_pressed(sf.Keyboard.UP):
    player.do_up()
  
  if sf.Keyboard.is_key_pressed(sf.Keyboard.LEFT):
    player.do_left()
    
  if sf.Keyboard.is_key_pressed(sf.Keyboard.RIGHT):
    player.do_right()
    
  if sf.Keyboard.is_key_pressed(sf.Keyboard.DOWN):
    player.do_down()
    
  if sf.Keyboard.is_key_pressed(sf.Keyboard.SPACE):
    player.do_fire(objects)
   
  # UPDATE
  for obj in objects:
    if obj.is_dead:
      objects.remove(obj)
    obj.update(dt)
 

  for objA in objects:
    if objA.collides_with is not None:
      for objB in objects:
        if objA.collides_with and objA.collides_with == objB.collision_class:
          if rect_intersect(objB.sprite.global_bounds, objA.sprite.global_bounds):
            objA.register_hit(objB)
            objB.register_hit(objA)
 
  px_shift += dt * px_speed
  background.update(dt, sf.Vector2(
    player.sprite.position.x, player.sprite.position.y + px_shift
  ))

  # DRAW  
  window.clear()
  window.draw(background)

  for obj in objects:
    window.draw(obj)

  ft = dt / 1000
  if ft > 9:
    print('Time: {:.1f}ms - {:.0f} FPS'.format(ft, 1000/ft))

  for i, t in enumerate(frames_time):
    bars[i].position = (bars[i].position.x, int(y_base_pos - t * 0.02))
    bars[i].size = (bars[i].size.x, t * 0.02)

  #for bar in bars:
  #  window.draw(bar)
  
  window.display()
  dt = clock.restart().microseconds
