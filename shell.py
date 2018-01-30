from sfml import sf
from entity import Entity


class Shell(Entity):
  SPEED = 0.001
  scale_factor = 0.1

  def __init__(self, *args, **kwargs):
    self.is_dead = False
    super().__init__(*args, **kwargs)
      
  def update(self, dt):
    self.sprite.move((0, -self.SPEED * dt))
    if self.sprite.position.y < 0:
      self.is_dead = True

  def draw(self, target, states):
    super().draw(target, states)
