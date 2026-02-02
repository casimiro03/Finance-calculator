import numpy as np
import matplotlib.pyplot as plt
import modules.database_handler as database_handler
from types import List, Any, Union, Dict




# Initialize the constructor method and inherit using super() method the instances variables of his parent class 'Database'
class Calculator(database_handler.Database):
  def __init__(self, database):
    super().__init__(database)
    self.rate = None
    self.money = None
    self.period = None
    self._future_value = None
    self._bulk_future_value = None


# Magic methods and _interfaces
  # __str__ Define what the program shows if your print() an object substituing for the viewer the object name in memory
  def __str__():
    pass

  # __it__ compare two objects a > b very similar to math logic connectors
  def __it__():
    pass


# financial methods
  def future_value(self,
                   rate: float,
                   price:int,
                   period:int
                   ):

    # Check if rate is a valid numeric type
    if not isinstance(rate, (int, float)):
        raise TypeError(f"Rate must be a numeric type (int or float), but got {type(rate)}")

    self.rate = rate
    self.price = price
    self.period = period

    self._future_value = price * (1+rate) ** period

    return self._future_value
    #print(f"the value of your {price} with an interest rate of {rate} on a period of {period} years will be {fv}")

    # should i make the future value variables object attributes or method attributes? # obj attributes if you want use them after the code block runs, method if you dont care after running



  #def calculate(self):
    #for each_elem in database:

# key question: how connect database object's values to get future value, and get future value to make operation using future value

  def bulk_future_value(self, period:int, price: int, database: any):

    self.period =period
    self.price =price
    self.database =database
    self._bulk_future_value =[]

    # matrixial class variables

    self.db = database_handler
    self.quantity = quantity
    self.period = period

    for i in database:
      if i is not None: # Added check for None values
        try:
            value = self.future_value(i, price, period) # Corrected map usage
            print(f"for the rate {i} in {period} years, your ${price} will ascend to {value}")
            self._bulk_future_value.append(value)
        except TypeError as e:
            print(f"Skipping invalid rate '{i}': {e}")
    return self._bulk_future_value

# Interfaces for the client to access to ADTs data
  def get_bulk_fv(self):
    return self._bulk_future_value

  def get_future_value(self):
    return self._future_value
# ----------------------------------
# Matrix operations
  def power_matrix(self, db: LIST, quantity: INT, period: INT):
    '''
    Discrete math code explanation
    '''
    self.db = db
    self.quantity = quantity
    self.period = period

    # the 1 is add to all elements of the array, matrix addition in other words a matrix addition add an elements for all elements in the matrix
    array_convertion = np.array(db) + 1
    # add 1 to avoid python 0 index problems 01234569 period is the nth term wich power the matrix
    N = period + 1

    #increasing=true make the progression go from the lower bound of the progression to the higher one, in layman terms the program will start with smaller amouts and the last result will be the biggers 'least bound of the set'
    m = np.vander(x, N, increasing=True)

    # this little one multiply all elemets of the matrix by m a binary operation in layman terms each elem of the matrix will be multiply by m using this matrix, vectorization in layman terms: instead of using a slow for loop this things do an operation more quickly
    self.binary_multiplication = m * money_quantity
    return self.binary_multiplication

  def data_view(self):
    for rate, db, axis in zip(self, ):
      # var definition
      y_values = axis
      x_values = np.arange(axis)
      # labels
      plt.title('future value of money over years')
      plt.ylabel('amout of money')
      plt.xlabel('years)')
      plt.plot()







# Tests

# Instance of the class Database (initialize db)


# Create a instance 'Calculator' passing mydb as the 'Database'
#portafolio= Calculator(fcis_porcentage)

# Define a variable that apply a bulk method to an instance
#check_portafolio = portafolio.bulk_future_value(5, 15000, fcis_porcentage)
#print(check_portafolio)



# Remember use the () in the print of the instance method call or the ouput will we the instance id instead of te expected data
#print(mydb.access_data())

"""
key question: how can i call the future_value function using list comprehession, passin the rate as the value to iterate, and
the period and money as something already defined

list comprehession is useful here cause i want call a function and apply that function to a larger dataset, list comprehession
is the pythonic way of do such thing the other option is write a larger function manually that do the same, apply a function

is possible call a method insde the arg of other method?

yes is possible and it is called function composotion / method (chaning / nesting)
if python see a nesting function the program stop, execute the inner function inside args, then execute the outside function
it's like math algebra composite function f(g(x)) 1st solve g(x) then f()
"""
mydb =Database(database_handler)
mydb.data_filt()
new_db =mydb.get_filter_data()

portafolio = Calculator(new_db)
y =portafolio.bulk_future_value(5,15000,new_db)

class Data_visualization():
  def __init__(x_values, y_values):

    self._y_values =y_values
    self._x_values =x_values
