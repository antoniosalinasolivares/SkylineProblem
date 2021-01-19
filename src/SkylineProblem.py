# Constants
Li = 0
Ri = 1
Hi = 2
SHOW_SOLUTION = True

class Skyline:
  # Attributes
  input_list = []
  solution = []
  holder = []
  
  # Stores the input and creates an array to hold data
  def __init__(self, input_list, show_solution = False):
    self.input_list = input_list
    self.holder = [0] * (self.getMax() + 1)
    if(show_solution):
      self.solve()
      print(self.solution)

  # Condenses the input list into one array
  def flatten(self):
    # Sorts the list by the value of Y 
    self.input_list.sort(key = lambda x : x[Hi])
    for item in self.input_list:
      for number in range(item[Li], item[Ri]):
        self.holder[number] = item[Hi]

  # uses the flattened array to create and return the solution
  def solve(self):
    if (self.solution):
      return self.solution
    self.flatten()
    self.solution = [ [index, self.holder[index]] 
                     for index in range (len(self.holder))
                      if self.holder[index] != self.holder[index-1]]
    return self.solution

  # Returns the top max value of X
  def getMax(self):
    for item in self.input_list:
      a = 0
      if(item[Ri] >= a):
        a = item[Ri]
    return(a)

test_input = [[2,9,10],[3,6,15],[5,12,12],[13,16,10],[15,17,5]]
test_solution = Skyline(test_input, SHOW_SOLUTION)

test_inputs = [
               [[1,11,6],[2,6,7],[4,13,10],[7,12,16],[3,15,25],[18,19,22],[13,23,29],[4,24,28]],
               [[3,9,10],[6,7,15],[5,11,12],[14,21,13],[19,24,8]],
               [[0,2,3],[2,5,3]],
               ]

for input in test_inputs:
    Skyline(input, SHOW_SOLUTION)
