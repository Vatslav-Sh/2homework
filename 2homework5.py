class BadClass:

   def __init__(self, val=0):
       self.__val = val

   def get_val(self):
        return self.__val

   def __hash__(self):
       return hash(self.__val)

   def __eq__(self, other):
       return isinstance(other, BadClass) and self.get_val() == other.__val


bad = BadClass(val=0)
even_worse = {bad}
assert bad in even_worse
print('yeah, wee good!')
