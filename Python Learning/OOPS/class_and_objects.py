class abc:
  __slots__ = ["name","age","clg"]
  def setter(self,name,age):
    self.name = name
    self.age = age
  def getter(self):
    print(f"Name : {self.name}")
    print(f"Age : {self.age}")

obj = abc()
obj.setter("Vishnu",23)
obj.getter()
# abc.clg = "LPU"
obj.clg = "MBU"
# print(obj.__dict__)
print(obj.name)



"""Create a BankAccount class with account_holder and balance. Add a display() method that displays the account details."""

class Banking:
  def __init__(self,account_holder,balance=0):
    self.account_holder = account_holder
    self.balance = balance
  def deposit(self,deposit):
    self.balance += deposit
  def display(self):
    print(f"Account_holder : {self.account_holder}\nBalance : {self.balance}")

C1 = Banking('Vishnu')
C1.deposit(10000)
C1.display()


"""Create two Cart objects. Add different products to each cart and prove that their lists are independent.
"""

class Cart:
  def __init__(self,name):
    self.name = name
    self.cart = []
  def display(self):
    print(self.name)
    print(f"Cart : {self.cart}")

c1 = Cart("Vishnu")
c2 = Cart('Virat')

c1.cart.append('Iphone')
c2.cart.append('Xiomi')

c1.display()
c2.display()

print(c1.cart is c2.cart)


"""Lets create spotify basic class with add_songs, remove_song and show_songs methods. Create a playlist and add songs to it. Remove a song from the playlist and display the remaining songs."""

class Spotify:
  def __init__(self,playlist_name):
    self.playlist_name = playlist_name
    self.playlist = []
  def add_songs(self,song_name):
    self.playlist.extend(song_name)
    print("Songs successfully added...")
  def remove_song(self,song):
    for i in song:
      if i in self.playlist:
        self.playlist.remove(i)
    print('Song removed successfully...')
  def show_songs(self):
    for num,song in enumerate(self.playlist,start = 1):
      print(num,song)
    
u1 = Spotify("Melody")
u1.add_songs(["Ninnu_kori","i wanna fly","kallumusi"])
u1.remove_song(["Ninnu_kori"])
u1.show_songs()


