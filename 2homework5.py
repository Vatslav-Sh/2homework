class BadClass:

   def __init__(self, val=0):
       self.val = val
       self.val2 = val

       """
       __init__ - это в основном функция, которая будет
       "инициализировать" / "активировать" свойства класса
       для определенного объекта. Другое определение метода __init__ — это конструктор.
       """



   def __hash__(self):
       return hash(self.val2)

   """
   __hash__ Позволяет настраивать хеширование объектов
   """



   def __eq__(self, other):
       return self.val == other.val

   """
   __eq__ Позволяет реализовать проверку на равенство
   для экземпляров пользовательских типов. object.
   """



bad = BadClass()

even_worse = { bad }

assert(bad in even_worse)

bad.val += 1

assert(bad in even_worse)

print('yeah, we good!')