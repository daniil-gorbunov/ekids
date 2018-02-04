from sfml import sf
from entity import Entity
from math import sin
from random import random, randrange

TRANPARENT_WHITE = sf.Color(255, 255, 255, 255)


class Enemy(Entity):
  SPEED = 0.000006
  hp = 3
  scale_factor = 0.5
  hit_anim_start = 0
  hit_anim_phase = 255
  hit_anim_duration = .7
  hit_anim_progress = False
  amp = 0
  phase = 0
  x0 = 0
  collision_class = 'enemy'

  def __init__(self, *args, **kwargs):
    self.phase = random() * 10
    self.amp = randrange(100, 200)
    self.SPEED *= randrange(-100, 100) / 100
    super(Enemy, self).__init__(*args, **kwargs)

  def update(self, dt):
    if self.x0 == 0:
      self.x0 = self.sprite.position.x
    
    self.phase += dt * self.SPEED
    
    self.sprite.position = (
      self.x0 + self.amp * sin(self.phase),
      self.sprite.position.y
    )
    
    if self.hit_anim_progress:
      incr = int(dt / self.hit_anim_duration / 1000)
      self.hit_anim_phase += incr
      if self.hit_anim_phase > 255:
        self.hit_anim_progress = False
        return
      self.sprite.color = sf.Color(255, self.hit_anim_phase, self.hit_anim_phase)

  def draw(self, target, states):
    super().draw(target, states)

  def register_hit(self, obj):
    obj.is_dead = True
    self.hp -= 1
    self.animate_hit()
    if self.hp <= 0:
      self.is_dead = True
    
  def animate_hit(self):
    self.hit_anim_progress = True
    self.hit_anim_phase = self.hit_anim_start
