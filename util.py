def rect_intersect(a, b):
  dx = a.left - b.left
  if a.width > -dx and b.width > dx:
     dy = a.top - b.top
     if a.height > -dy and b.height > dy:
      return True
  return False
