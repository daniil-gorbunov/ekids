from sfml import sf


class ParallaxeBackground(sf.TransformableDrawable):
  def __init__(self, textures, target_width):
    self.textures = textures
    
    self.layers = []
    for texture in textures:
      texture.smooth = False
      texture.repeated = True
      size = texture.size
      scale_factor = target_width / size.x
      layer = sf.Sprite(texture)
      layer.scale((scale_factor, scale_factor))
      self.layers.append(layer)
    
    super(sf.TransformableDrawable, self).__init__()
    
  def update(self, dt, offset):
    for i in range(len(self.layers)):
      layer = self.layers[i]
      offset_x = offset.x * ((i + 1) / 30) / layer.ratio.x
      offset_y = offset.y * ((i + 1) / 40) / layer.ratio.y
      layer.texture_rectangle = (offset_x, offset_y, layer.local_bounds.width, layer.local_bounds.height)

  def draw(self, target, states):
    for layer in self.layers:
      target.draw(layer)

