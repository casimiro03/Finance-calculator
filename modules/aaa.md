What the **self**  keyword do? it works as the blueprint for the instances. thats the reasons why we use self.value is the blueprint for the value of the instance.


How we call the attributes of a superclass?

using the super() method

super.__init__(self, x)

super start in the new object the __init__ method of the superclass parent class, to his lovely child.


why the database it's a nested dict of dicts?
we can use a relational database as a common industry pracrice, the selection of dicts is for educative porpuses and quick deployment. this avoid create an database using postegre, or sqlite.


magic methods:

__init__ this one initialize the data attributes of the class once the class is called in a instance. and once we define our data attributes we can use them in any place of the object.



---

what happen if i declare variables outside the __init__ body function?

without a self.var they disappear after the method is executed, and such var dont returned

---


### Should IDeclarate args in the constructor magic method, vs in methods:


summary the what: args declare in the __init__ method are persistent with the object created the instance, args declarated in a method are use only once and then lost. the only way they wouldnt be lost is make the self.x


---




### I want visualize the output of a class's method, what can go wrong?

when your print an instance method remember use the(example):

mydb = Database(dicts_database)
print(mydb.access_data()) # This

expected output (for the specific adt):

[0.1236, 0.3792, 0.3505, None, 0.0249, 0.2235, 0.49, 0.3816, 0.228]

or the program will return an object if if you use the:

print(mydb.access_data)


and the output will look like this:

<bound method Database.access_data of <__main__.Database object at 0x7bbbcb717140>>

----



### unsure if declare an instance variable inside a method or in the constructuor class

, cuz i need utize financial methods, in the class. which will broke the program in what cases?

the pros: in make the code clear to read, at first(less instance variables in the constructor method definition)

the constras: i will need call 1st the method with the instance variables, before use it in other methods(if they use that instance variables), in the bigenning it dosnt looks bad, cause i think: the methods that use the same variables, will be used after the method with the instance variables, example future value, then modeling. but i didnt tought in the case of similar data(instane variabls) but unncesary between them: example calculate the inflation, call the future value will be computational worthless.


for such problems we can declare instance variable which a none type, and later in the code once we need them in a method, we can assign them another data type: bounding the better of the 2 worlds avoid the neccsity of define such variable when isnt neccesary, and have it in globally in the created object.

its like know a person, you know it's name and maybe no her birthday yet, you know she have a name, but you dont know it already, later when you know she more, she can comment you her birthday data, and with that information you can use methods, like "greet for birthday" or "give her a gift in her birthday".

self.rate = none
self.period = none
self.money_quantity = none


---

### how can i apply a method / function to other function f(g(x))? why? cuz i want bulk apply a function to a dataset.

there are 3 posibble ways:

list comprehession, mapping and a for loop

**mapping**: doenst create the list in method instantly it pass one by one value.

**comprehession**: it's like set builder notation and the pythonic way: S = [x of the real numbers: 0>=1000]

values = database
[future_value(rate, price, value) for x in dataset]

---


key question:

how add title index and sections to a md document for easy code review.


---

### philospy:

code is like grow a garden, as complexity of the code grow programmers have two ways to make things: brake a problem into smaller parts modularize, and create abstraction. from this idea we have adts, code that is created with a porpuse to manipulate data attributes, methods and algoritgms to operate data and return values.

this is very similar to grow a garden with enough time someone can create complex resusable and useful adts that work togheter in a system using objects to modularize programs. this make me think a lot in miguel o'hara and lyla or palantir technogy, create software that work togheter, and can be command to do ceertain taks when someone want always using adts, like nodes for politics and finance based in the same adt object. it's amazing and this is the biggening of my garden.





# verify if this is useful for the docu or erase

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


#Why use matrixes and vectorization?
for loops are slow and thinking ahead in the program life, and inspired in the idea of software as a garden. i decide from a early stage of development use vectorization a very used tools of scitific computing to make my program run faster in larger datasets, and belive me when i say data can became really tricky in bigger datasets

[add draw by me]




---

# Import modules

27/1/2026 today was the day i decide refactorize my codebase. Why? googlecolab is exellent for scietific computing portability and notetaking.
but my program grew bigger and i need modularize parts in order to improve reability, as start thinking about the architecture of the program.

how import modules in python?

import module_name as new_name *this is useful cuz module_name rename avoid overlapping names in the code and provide abreviations for longer names*

another variant programmers use but is considerate difficult to read is:

from M import * *many python programmers think this version is difficult to read cuz isno longer abvious whee a name is define therefore overlap the program the "wild card import"*


# File management - how write and save files?
For more information see: Intro to CS and Programming Using Python - Guttang - MIT Press 3ed, section 7.1 Files

Here is the digitized text from the image, organized for easy reference in your documentation.

## Python File Handling Reference

| Method / Command | Description |
| --- | --- |
| `open(fn, 'w')` | **fn** is a string representing a file name. Creates a file for **writing** and returns a file handle. |
| `open(fn, 'r')` | **fn** is a string representing a file name. Opens an existing file for **reading** and returns a file handle. |
| `open(fn, 'a')` | **fn** is a string representing a file name. Opens an existing file for **appending** and returns a file handle. |
| `fh.read()` | Returns a **string** containing the contents of the file associated with the file handle **fh**. |
| `fh.readline()` | Returns the **next line** in the file associated with the file handle **fh**. |
| `fh.readlines()` | Returns a **list**, each element of which is one line of the file associated with the file handle **fh**. |
| `fh.write(s)` | Writes the **string s** to the end of the file associated with the file handle **fh**. |
| `fh.writelines(S)` | **S** is a sequence of strings. Writes **each element of S** as a separate line to the file associated with the file handle **fh**. |
| `fh.close()` | **Closes** the file associated with the file handle **fh**. |

---

> **Note:** When using `open()`, it is a best practice in modern Python to use a `with` statement (context manager) to ensure the file handle is closed automatically, even if an error occurs.

Would you like me to provide a few code examples showing how these methods work in a real script?