from sfml import sf
from entity import Entity
from shell import Shell


class Player(Entity):
  SPEED = 0.0005
  FIRE_RATE = 5
  fire_dt = 0
  idle_texture = None
  active_texture = None
  scale_factor = 0.5
  move_h = 0
  move_v = 0

  def __init__(self, idle_texture, *args, **kwargs):
    self.idle_texture = idle_texture
    self.sprite = sf.Sprite(idle_texture)
    self.sprite.scale((self.scale_factor, self.scale_factor))
    size = idle_texture.size
    self.sprite.origin = (size.x / 2, size.y / 2)
    super(Player, self).__init__(*args, **kwargs)
      
  def update(self, dt):
    if self.move_h or self.move_v == -1:
      self.sprite.texture = self.active_texture
    else:
      self.sprite.texture = self.idle_texture
    
    self.sprite.move((self.move_h * self.SPEED * dt, self.move_v * self.SPEED * dt))
    self.sprite.rotation = self.move_h * 5
    self.move_h = 0
    self.move_v = 0

    self.fire_dt += dt


  def draw(self, target, states):
    super().draw(target, states)

  def do_up(self):
    self.move_v = -1
    
  def do_down(self):
    self.move_v = 1
    
  def do_left(self):
    self.move_h = -1
    
  def do_right(self):
    self.move_h = 1
    
  def do_fire(self, objects):
    if self.fire_dt > 1000000 / self.FIRE_RATE:
      shell = Shell(-self.move_v * self.SPEED)
      shell.scale_factor = 1.75
      shell.setSprite(self.shell_texture)
      shell.sprite.position = self.sprite.position
      objects.append(shell)
      self.fire_dt = 0
