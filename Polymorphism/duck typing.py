class circle:
   def draw(self):
      print ("Draw a circle")
      return

class rectangle:
   def draw(self):
      print ("Draw a rectangle")
      return

class area:
   def area(self):
      print ("calculate area")
      return

def duck_function(obj):
   obj.draw()

objects = [circle(), rectangle(), area()]
for obj in objects:
   duck_function(obj)