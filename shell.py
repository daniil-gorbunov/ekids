from sfml import sf
from entity import Entity


class Shell(Entity):
  SPEED = 0.001
  scale_factor = 0.1
  collides_with = 'enemy'

  def __init__(self, offset_speed, *args, **kwargs):
    self.speed = self.SPEED + offset_speed
    self.is_dead = False
    super().__init__(*args, **kwargs)
      
  def update(self, dt):
    self.sprite.move((0, -self.speed * dt))
    if self.sprite.position.y < 0:
      self.is_dead = True

  def draw(self, target, states):
    super().draw(target, states)
