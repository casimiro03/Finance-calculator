# Create object and an ADT
class Database(object):

  def __init__(self, database):
  # Initialize the instance variable for future use in this class
    self.database =database
    self._L1 =[]

#convention to say to devs and reviewes 'this isnt suposse to be accesed by the user'
  # This method access data attributes in the db and operate them
  def data_filt(self):
    """ Values declaration:
    k: The key is a string
    database: A dict (data) which values are dicts (fcis).
    dcits fci contain a dict with 3 values: broker_name, valor, moneda
    """

    # define a variable with the value of each key
    # access key's values

    for k in self.database:

      DictValues = self.database[k]


      NestedDictValue = DictValues.get('valor')
      # The method get() return the values of an item with an specified key.
      self._L1.append(NestedDictValue)

    return None

  def get_filter_data(self):
      print(self._L1)
      return self._L1






#Use super().__init__(name) to invoke the __init__ function of its super class.


