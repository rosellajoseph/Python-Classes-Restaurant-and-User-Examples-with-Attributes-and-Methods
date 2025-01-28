#CLASSES
#making an object from a class is called instantation and you work with instances of a class.
#CREATING the Dog Class
#STEP 1 define the class
#In this step we are simply creating a class named Resteraint using the class keyword
#Step 2 Define the init()method
#Step 3: Store attributes in init() method
#step 4:Define the describe_resteraunt() method
#In this step we use the self keyword (which refers to the instance of the class) to store the restaraunt_name and cuisine_tpe passed to the contructor (__init_())  as attrobutess of the class
#Step 5:Implement the describe_resteraunt() method 
#This step fills in the 'describe'
#Step 6: Define the open_resteraunt() method
#step 7:Implement the open_resteraunt() method
class Restaurant:
  def __init__(self, restaurant_name, cuisine_type):
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type

  def describe_restaurant(self):
    print(f"Restaurant name: {self.restaurant_name}")
    print(f"Cuisine type: {self.cuisine_type}")

  def open_restaurant(self):
    print(f"The restaurant {self.restaurant_name} is now open!")
  #Create an instance of the Restaurant class
restaurant = Restaurant("McDonalds", "Red Lobster")   
#Call the describe_resterant method with a descriptive message
print("Describing the restaurant:")
restaurant.describe_restaurant()
#Call the open_restaurant with a message indicating the action
print("Opening the restaurant:")
restaurant.open_restaurant()
#Create Instances 
#To create instances from the class you simply use the calss name followed by parantheses just like calling a function
restaurant1 = Restaurant("Restaurant A", "Haitian")
restaurant2 = Restaurant("Restaurant B","Italian")
restaurant3 = Restaurant("Restaurant C","Chinese")                         
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()  
restaurant3.describe_restaurant()
#USERS 
#FACEBOOK EXAMPLE TUTORIAL
class User:
  pass
user1 = User()
#user1 is an instance of Uuser1 = User()
#Field:Data attached to an object
#Style Guide for Python
#lowercase with words seperated by underscores as nessary to improve readability
user1.first_name = "Dave"
user1.last_name = "Jones"
print(user1.first_name)
print(user1.last_name)
first_name = "Arthur"
last_name = "Smith"
#To put whole name
print(first_name, last_name)
print( user1.first_name, user1.last_name)
user2 = User()
user2.first_name = "Rosella"
user2.last_name = "Joseph"
print(first_name, last_name)
print(user2.first_name, user2.last_name)
user1.age = 25
user2.favorite_book = "The Mortal Instruments: City of Bones"
print(user1.age)
print(user2.favorite_book)
class User:
 def __init__(self,full_name,birthday):
  self.name =full_name
  self.birthday = birthday
  name_pieces  = full_name.split(" ")
   self.first_name = name_pieces
user= User ("Rosella Joseph", "June 13th 1996")
print(user.name,user.birthday)
 #SPLIT METHOD
sentence ="The quick brwon fox"
words=sentence.split()
print(words)