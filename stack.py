DEBUG = True



class stack:
  def __init__(self, n):
      self.container = [[]]
      self.nStacks = 0
      self.threshold = n
      self.size=0

  def push(self, val):
      if (self.size +1) % self.threshold == 0:
          self.nStacks += 1
          self.container.append([])
          self.container[self.nStacks].append(val)
          if DEBUG:
              print " created nth stack"
          self.size= self.size +1

      else:
          self.container[self.nStacks].append(val)
          self.size = self.size+1
  
  def print_stack(self):
       for i in self.container:
           for j in i:
               print j



st = stack(5)
for i in range (15):
    st.push(i)

st.print_stack()
