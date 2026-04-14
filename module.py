# In main file
# import script1
# print(script1.sum(1, 3))

# You will need to add code in this module to make teh Point of Sale Application functional.


class PointOfSale:
  def __init__(self):
    self.checkout_total = 0 # This is an example varialbe, remove it or change it as you please.
    print("\nInitializing POS system...")
  Cart = []
  def Show_cart(self):
    for i in cart:
      index = 0 
      i = cart[index]
      print(i)
      index += 1 
    if cart is []:
      print("Your cart is empty")


  
    
  def start(self):# This is the function that should be used to start the application. 
    print("\n=================================")
    print("MENU:Please choose an option seen below")
    print("1. Show Cart")
    print("2. Add To Cart")
    print("3. Show Checkout Total")
    print("4. Checkout")
    print("5. EXIT")
    print("=================================")

    choice = input("\nEnter Selection:")
    if choice == "1":
      print("pulling up cart...")
      self.Show_cart()





