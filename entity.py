from sfml import sf
from params import draw_bbox


class Entity(sf.TransformableDrawable):
  collides_with = None
  collision_class = None
  
  def __init__(self):
    self.global_bbox_rect = sf.RectangleShape()
    self.global_bbox_rect.outline_color = sf.Color.GREEN
    self.global_bbox_rect.outline_thickness = -1
    self.global_bbox_rect.fill_color = sf.Color.TRANSPARENT
    
    self.local_bbox_rect = sf.RectangleShape()
    self.local_bbox_rect.outline_color = sf.Color.RED
    self.local_bbox_rect.outline_thickness = -1
    self.local_bbox_rect.fill_color = sf.Color.TRANSPARENT
    
    self.scale_factor = 1
    self.pool = []
    self.is_dead = False
    
    self.draw_bbox = draw_bbox
    
    super(sf.TransformableDrawable, self).__init__()
    
  def setSprite(self, texture):
    self.sprite = sf.Sprite(texture)
    self.sprite.scale((self.scale_factor, self.scale_factor))
    size = texture.size
    self.sprite.origin = (size.x / 2, size.y / 2)
    
  def update(self, dt):
    pass

  def draw(self, target, states):
    #states.transform.combine(self.transformable.transform)
    target.draw(self.sprite)
    if self.draw_bbox:
      bbox = self.sprite.global_bounds
      self.global_bbox_rect.position = (bbox.left, bbox.top,)
      self.global_bbox_rect.size = (bbox.width, bbox.height,)
      target.draw(self.global_bbox_rect)

  def register_hit(self, obj): pass
