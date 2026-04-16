# In main file
# import script1
# print(script1.sum(1, 3))

# You will need to add code in this module to make teh Point of Sale Application functional.


class PointOfSale:
  def __init__(self):
    self.checkout_total = 0 # This is an example varialbe, remove it or change it as you please.
    print("\nInitializing POS system...")
    self.Cart = []
    
  
  def Show_cart(self):
    if len(self.Cart) == 0:
      print("Your cart is empty")
      return
    for i in range(0,len(self.Cart)):
     print(self.Cart[i])

  def Add_cart():
    product = input("what product do you want to add?")
    price = input("Enter the price of this item")
    return
    
      


  
    
  def start(self):# This is the function that should be used to start the application. 
    while True:
      print("\n=================================")
      print("\nMENU:Please choose an option seen below")
      print("1. Show Cart")
      print("2. Add To Cart")
      print("3. Show Checkout Total")
      print("4. Checkout")
      print("5. EXIT")
      print("=================================")
      choice = input("\nSelection Entered:")
      
      if choice == "1":
        print("pulling up cart...")
        self.Show_cart()
        
        if choice == "2":
          print("Pulling up product addtion panel...")
          self.Add_cart()





