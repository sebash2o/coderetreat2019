import os, sys

#w, h = 5, 5;
#m = [[0 for x in range(w+2)] for y in range(h+2)] 

def display_game(m):
  for x in range(1, w+1):
    s = ""
    for y in range(1, h+1):
      s += str(m[x][y])
    print (s)

class GameOfLife:

  def __init__(self, m):
    self.m = m[:]
    self.w = len(m)
    self.h = len(m[0])

  def count_neighbours(self, (x,y)):
    num = 0
    #print(len(self.m))
    #print(len(self.m[0]))
    for i in range (x-1,x+2):
      for j in range (y-1,y+2):
        if (i != x or j != y) and 0 <= i < self.h and 0 <= j < self.w:
          print (i, j)
          num += self.m[i][j]
    return num

  def is_underpopulated(self, (x,y)):
    return self.count_neighbours((x,y)) < 2

  def is_overpopulated(self, (x,y)):
    return self.count_neighbours((x,y)) > 3

  def is_live_on(self, (x,y)):
    return 2 <= self.count_neighbours((x,y)) <= 3 

  def is_spawn(self, (x,y)):
    #return True
    return self.count_neighbours((x,y)) == 3

  def evolve_cell(self, current):
    (x,y) = current
    next_c = self.m[x][y]
    # under, over
    #if self.is_underpopulated(current) or self.is_overpopulated(current): next_c = 0
    if not self.is_live_on(current): next_c = 0
    # spawn
    if self.is_spawn(current): next_c =  1
    # live on - do nothin
    return next_c

  def evolve(self):
    next_m = []
    for x in range(0, self.h):
      next_r = []
      for y in range(0, self.w):
        current = (x, y)
        next_r.append(self.evolve_cell(current))
      next_m.append(next_r)
    self.m = next_m
    return next_m

class TestGame:

  def test_should_return_zero_when_all_neighbours_are_dead(self):
    m = [ [0, 0, 0],
          [0, 1, 0],
          [0, 0, 0] ]
    assert GameOfLife(m).count_neighbours((1,1)) == 0

  def test_should_return_8_when_all_neighbours_are_alive(self):
    m = [ [1, 1, 1],
          [1, 1, 1],
          [1, 1, 1] ]
    assert GameOfLife(m).count_neighbours((1,1)) == 8

  def test_should_return_1_when_1_neighbour_is_alive(self):
    m = [ [1, 0, 0],
          [0, 1, 0],
          [0, 0, 0] ]
    assert GameOfLife(m).count_neighbours((1,1)) == 1

  def test_should_return_1_when_1_neighbour_is_alive(self):
    m = [ [1, 0, 0],
          [0, 1, 0],
          [0, 0, 0] ]
    assert GameOfLife(m).count_neighbours((0,0)) == 1

  def test_is_underpopulated_1_neighbour(self):
    m = [ [1, 0, 0],
          [0, 1, 0],
          [0, 0, 0] ]
    assert GameOfLife(m).is_underpopulated((1,1)) == True

  def test_is_underpopulated_2n(self):
    m = [ [1, 0, 0],
          [0, 1, 0],
          [0, 1, 0] ]
    assert GameOfLife(m).is_underpopulated((1,1)) == False

  def test_is_overpopulated_1_neighbour(self):
    m = [ [1, 0, 0],
          [0, 1, 0],
          [0, 0, 0] ]
    assert GameOfLife(m).is_overpopulated((1,1)) == False

  def test_is_overpopulated_2n(self):
    m = [ [1, 0, 0],
          [0, 1, 0],
          [0, 1, 0] ]
    assert GameOfLife(m).is_overpopulated((1,1)) == False

  def test_is_overpopulated_3n(self):
    m = [ [1, 0, 0],
          [0, 1, 1],
          [0, 1, 0] ]
    assert GameOfLife(m).is_overpopulated((1,1)) == False

  def test_is_overpopulated_4n(self):
    m = [ [1, 0, 0],
          [0, 1, 1],
          [1, 1, 0] ]
    assert GameOfLife(m).is_overpopulated((1,1)) == True

  def test_is_live_on_1n(self):
    m = [ [1, 0, 0],
          [0, 1, 0],
          [0, 0, 0] ]
    assert GameOfLife(m).is_live_on((1,1)) == False

  def test_is_live_on_2n(self):
    m = [ [1, 0, 0],
          [1, 1, 0],
          [0, 0, 0] ]
    assert GameOfLife(m).is_live_on((1,1)) == True

  def test_is_live_on_3n(self):
    m = [ [1, 0, 0],
          [1, 1, 1],
          [0, 0, 0] ]
    assert GameOfLife(m).is_live_on((1,1)) == True

  def test_is_live_on_4n(self):
    m = [ [1, 0, 0],
          [1, 1, 1],
          [0, 0, 1] ]
    assert GameOfLife(m).is_live_on((1,1)) == False

  def test_is_spawn_1n(self):
    m = [ [1, 0, 0],
          [0, 1, 0],
          [0, 0, 0] ]
    assert GameOfLife(m).is_spawn((1,1)) == False

  def test_is_spawn_2n(self):
    m = [ [1, 0, 0],
          [1, 1, 0],
          [0, 0, 0] ]
    assert GameOfLife(m).is_spawn((1,1)) == False

  def test_is_spawn_3n(self):
    m = [ [1, 0, 0],
          [1, 1, 1],
          [0, 0, 0] ]
    assert GameOfLife(m).is_spawn((1,1)) == True

  def test_is_spawn_4n(self):
    m = [ [1, 0, 0],
          [1, 1, 1],
          [0, 0, 1] ]
    assert GameOfLife(m).is_spawn((1,1)) == False

  def test_complex_test_1(self):
    m1 = [ [1, 1, 0],
          [1, 0, 0],
          [1, 1, 1] ]
    m2 = [ [1, 1, 0],
          [0, 0, 1],
          [1, 1, 0] ]
    assert GameOfLife(m1).evolve() == m2
    
