class RRIter(object):
  def __init__(self, rrlist):
    self.rrlist = rrlist
    self.idx = 0
  
  def __iter__(self):
    return self
    
  def __next__(self):
    if self.idx >= self.rrlist.size:
      raise StopIteration
    ret = self.rrlist.pool[
      (self.idx + self.rrlist.head_idx) % self.rrlist.size
    ]
    self.idx += 1
    return ret

class RoundRobin(object):
  def __init__(self, size, init=None):
    self.size = size
    self.head_idx = 0
    
    # Initialize pool
    self.pool = [init] * size
  
  def _incr_head(self):
    self.head_idx += 1
    if self.head_idx == self.size:
      self.head_idx = 0
  
  def __iter__(self):
    return RRIter(self)
    
  def __len__(self):
    return self.size
    
  def add(self, item):
    self.pool[self.head_idx] = item
    self._incr_head()
