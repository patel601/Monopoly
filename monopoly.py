
#properties of each place and data attained from -- https://en.wikibooks.org/wiki/Monopoly/Official_Rules --
# modules attained from w3resources.com

import math
import random
import sys

# module attained from meccanismocomplesso.org


# make a class that has the specific parameters (sys) that has options of what to do when a player lands on that piece
# def __init__ --> is a code tag for something with more than one attribute, like a car... so each space in the game has more than one attribute
# ^^ code tag above is attained from micropyramid.com


class player:
   def __init__(self, name, place, money, jailcard, timeinjail, diceroll, gamepiece, secondaccount, user):
       self.name = str(name)
       self.money = int(money)
       self.jailcard = int(jailcard)
       self.timeinjail = int(timeinjail)
       self.diceroll = int(diceroll)
       self.gamepiece = gamepiece
       self.place = place
       # list for colors (index 0-7)
       self.newlist = [[], [], [], [], [], [], [], []]
       self.rrlist = []
       self.utilitylist = []
       self.secondaccount = int(secondaccount)
       self.user = int(user)

   # add a def for a new owner of a house or whatever..... new owner is the name... total money=current-newhouse


   def newowner(self, newproperty):
       newproperty.owner = self.name
       self.money = self.money - newproperty.price
       prop = 0
       # add according to color
       # create a loop saying if it was a certain color, add 1-whatever
       # drk blue--0;green--1;yellow--2;red--3;orange--4;pink--5;lgtblue--6;purple--7;
       while prop == 0:
           # https://docs.python.org/2/library/functions.html----- isinstance function
           if isinstance(newproperty, Property):
               if newproperty.color == "darkblue":
                   list = 0
               if newproperty.color == "green":
                   list = 1
               if newproperty.color == "yellow":
                   list = 2
               if newproperty.color == "red":
                   list = 3
               if newproperty.color == "orange":
                   list = 4
               if newproperty.color == "pink":
                   list = 5
               if newproperty.color == "lightblue":
                   list = 6
               if newproperty.color == "purple":
                   list = 7
               # addlist ---- append it

               self.newlist[list].append(newproperty)
               prop = 1

           if isinstance(newproperty, rrbox):
               self.rrlist.append(newproperty)
               prop = 1
           if isinstance(newproperty, utility):
               self.utilitylist.append(newproperty)
               prop = 1

       for colorlist in self.newlist:
           if len(colorlist) == 2:
               for pp in colorlist:
                   if pp.color == "purple":
                       colorlist.append("monopoly")
                       break
                   if pp.color == "darkblue":
                       colorlist.append("monopoly")
                       break
           if len(colorlist) == 3:
               if "monopoly" not in colorlist:
                   colorlist.append("monopoly")
                   break




class BOX:
   def __init__(self):
       type = box


# property for each box----- property(box)
# make a class for each type of box --- tax, free, railroad, jail, chance, etc.
class Property(BOX):
#regular boxes with colors
   def __init__(self, name, type, position, price, cost, mortage, rent, x1, x2, x3, x4, x5, owner, color, house):
       # rename them for their own class
       self.name = name
       self.type = type
       self.position = position
       self.price = int(price)
       self.cost = int(cost)
       self.mortage = int(mortage)
       self.rent = int(rent)
       self.owner = owner
       # amount of times you buy the house
       self.x1 = int(x1)
       self.x2 = int(x2)
       self.x3 = int(x3)
       self.x4 = int(x4)
       self.x5 = int(x5)
       self.color = color
       self.house = int(house)





#chance
class Chancebox(BOX):
   def __init__(self, name, type, position):
       self.name = name
       self.type = type
       self.position = position





#communitychest
class CCbox(BOX):
   def __init__(self, name, type, position):
       self.name = name
       self.type = type
       self.position = position





#free space
class Freespacebox(BOX):
   def __init__(self, name, type, position):
       self.name = name
       self.type= type
       self.position = position


#jail
class jailbox(BOX):
   def __init__(self, name, type, position):
       self.name = name
       self.type= type
       self.position = position


#tax
class taxbox(BOX):
   def __init__(self, name, type, position, tax):
       self.name = name
       self.type= type
       self.position = position
       self.tax = tax



#utility--electric company&waterworks
class utility(BOX):
   def __init__(self, name, type, position, owner):
       self.name = name
       self.type= type
       self.position = position
       self.owner = owner
        #going back to the main box one i made... use that to assign a cost for this box
        #assign price u1,u2----bc you can buy it twice.... and mortage
        #float the price bc its money
       self.price = float(150)
       self.u1 = float(4)
       self.u2 = float(10)
       self.mortage = float(75)


#railroad
class rrbox(BOX):
   def __init__(self, name, type, position, owner):
       self.name = name
       self.type = type
       self.position = position
       self.owner = owner
       # do the same thing as utlity
       # assign price, r1-4, mortage
       self.price = float(200)
       self.r1 = float(25)
       self.r2 = float(50)
       self.r3 = float(100)
       self.r4 = float(200)
       self.mortage = float(100)






# CARDS
class CommunityChest:
   def __init__(self, description, go, collect, amountdue, housecost, nojail, jail, collect50d):
       self.description = description
       self.go = int(go)
       self.collect = int(collect)
       self.amountdue = int(amountdue)
       self.housecost = int(housecost)
       self.nojail = nojail
       self.jail = jail
       self.collect50d = collect50d



#most things are the same for chance

class Chance:
   def __init__(self, description, go, collect, amountdue, housecost, nojail, jail, goback):
       self.description = description
       self.go = int(go)
       self.collect = int(collect)
       self.amountdue = int(amountdue)
       self.housecost = int(housecost)
       self.nojail = nojail
       self.jail = jail
       self.goback = goback





#class players
#assign a name, place on board, money, jailcard, timeinjail, diceroll, gamepiece)



   def buyhouse(self, newprop):
       for colorlist in self.newlist:
           for pp in colorlist:
               if newprop.name == pp.name:
                   pp.house += 1


   def mortageprop(self, newprop):
       self.money += newprop.mortage
       for colorlist in self.newlist:
           for pp in colorlist:
               if newprop.name == pp.name:
                   colorlist.remove(pp)
       for rail in rrlist:
           if newprop.name == rail.name:
               rrlist.remove(rail)
       for ut in utilitylist:
           if newprop.name == ut.name:
               utilitylist.remove(ut)




#gameboard

class board:
   def __init__(self, players, piece):

       # array of players playing the game
       self.listofplayers = []

       gamepieces = ["Battleship", "Wheelbarrow", "Iron", "Wheel", "Horse", "Car", "Shoe", " Thimble", "Terrier",
                     "Hat"]
       for gp in gamepieces:
           if piece == gp:
               gamepieces.remove(gp)
       # (self, name, place, money, jailcards, time in jail, dice roll, game piece, secondaccount, user
       user = player("Player", 0, 1500, 0, 0, 0, piece, 0, 1)
       self.listofplayers.append(user)




       for i in range(1, int(players) + 1):
           numberofplayers = i+1
           computer = random.choice(gamepieces)
           gamepieces.remove(computer)
           print(str(computer))
           player2 = player(str("Computer"+str(numberofplayers)),0,1500,0,0,0,computer,0,0)
           self.listofplayers.append(player2)

   #gameboard

       self.boardlist= []

       gobox = Freespacebox("Go", "freespace", 1)
       self.boardlist.append(gobox)

       mediterraneanavenue = Property("Mediterranean Avenue", "property", 2, 60, 50, 30, 2, 10, 30, 90, 160, 250,
                                      "bank", "purple", 0)
       self.boardlist.append(mediterraneanavenue)

       cc1 = CCbox("Community Chest", "communitychest", 3)
       self.boardlist.append(cc1)

       balticavenue = Property("Baltic Avenue", "property", 4, 60, 50, 30, 4, 20, 60, 180, 320, 450, "bank", "purple",
                               0)
       self.boardlist.append(balticavenue)

       incometax = taxbox("Income Tax", "tax", 5, 200)
       self.boardlist.append(incometax)

       rr1 = rrbox("Reading Railroad", "railroad", 6, "bank")
       self.boardlist.append(rr1)

       orientalavenue = Property("Oriental Avenue", "property", 7, 100, 50, 50, 6, 30, 90, 270, 400, 550, "bank",
                                 "lightblue",
                                 0)
       self.boardlist.append(orientalavenue)

       chance1 = Chancebox("Chance", "chance", 8)
       self.boardlist.append(chance1)

       vermontavenue = Property("Vermont Avenue", "property", 9, 100, 50, 50, 6, 30, 90, 270, 400, 550, "bank",
                                "lightblue", 0)
       self.boardlist.append(vermontavenue)

       connecticutavenue = Property("Connecticut Avenue", "property", 10, 120, 50, 60, 8, 40, 100, 300, 450, 600,
                                    "bank",
                                    "lightblue", 0)
       self.boardlist.append(connecticutavenue)

       injail = Freespacebox("Jail", "freespace", 11)
       self.boardlist.append(injail)

       stcharles = Property("St. Charles Place", "property", 12, 140, 100, 70, 10, 50, 150, 450, 625, 750, "bank",
                            "pink",
                            0)
       self.boardlist.append(stcharles)

       utility1 = utility("Electric Company", "utility", 13, "bank")
       self.boardlist.append(utility1)

       statesavenue = Property("States Avenue", "property", 14, 140, 100, 70, 10, 50, 150, 450, 625, 750, "bank",
                               "pink", 0)
       self.boardlist.append(statesavenue)

       virginiaavenue = Property("Virginia Avenue", "property", 15, 160, 100, 80, 12, 60, 180, 500, 700, 900, "bank",
                                 "pink",
                                 0)
       self.boardlist.append(virginiaavenue)

       rr2 = rrbox("Pennsylvania Railroad", "railroad", 16, "bank")
       self.boardlist.append(rr2)

       stjames = Property("St. James Place", "property", 17, 180, 100, 90, 14, 70, 200, 550, 750, 950, "bank",
                          "orange", 0)
       self.boardlist.append(stjames)

       cc2 = CCbox("Community Chest", "communitychest", 18)
       self.boardlist.append(cc2)

       tennesseeavenue = Property("Tennessee Avenue", "property", 19, 180, 100, 90, 14, 70, 200, 550, 750, 950, "bank",
                                  "orange", 0)
       self.boardlist.append(tennesseeavenue)

       newyorkavenue = Property("New York Avenue", "property", 20, 200, 100, 100, 16, 80, 200, 600, 800, 1000, "bank",
                                "orange", 0)
       self.boardlist.append(newyorkavenue)

       freeparking = Freespacebox("Free Parking", "freespace", 21)
       self.boardlist.append(freeparking)

       kentuckyavenue = Property("Kentucky Avenue", "property", 22, 220, 150, 110, 18, 90, 250, 700, 875, 1050, "bank",
                                 "red",
                                 0)
       self.boardlist.append(kentuckyavenue)

       chance2 = Chancebox("Chance", "chance", 23)
       self.boardlist.append(chance2)

       indianaavenue = Property("Indiana Avenue", "property", 24, 220, 150, 110, 18, 90, 250, 700, 875, 1050, "bank",
                                "red", 0)
       self.boardlist.append(indianaavenue)

       illinoisavenue = Property("Illinois Avenue", "property", 25, 240, 150, 120, 20, 100, 300, 750, 925, 1100,
                                 "bank", "red",
                                 0)
       self.boardlist.append(illinoisavenue)

       rr3 = rrbox("B&O Railroad", "railroad", 26, "bank")
       self.boardlist.append(rr3)

       atlanticavenue = Property("Atlantic Avenue", "property", 27, 260, 150, 130, 22, 110, 330, 800, 975, 1150,
                                 "bank",
                                 "yellow", 0)
       self.boardlist.append(atlanticavenue)

       ventnoravenue = Property("Ventnor Avenue", "property", 28, 260, 150, 130, 22, 110, 330, 800, 975, 1150, "bank",
                                "yellow", 0)
       self.boardlist.append(ventnoravenue)

       utility2 = utility("Water Works", "utility", 29, "bank")
       self.boardlist.append(utility2)

       marvingardens = Property("Marvin Gardens", "property", 30, 280, 150, 140, 24, 120, 360, 850, 1025, 1200, "bank",
                                "yellow", 0)
       self.boardlist.append(marvingardens)

       gotojail = jailbox("Go To Jail", "gotojailspace", 31)
       self.boardlist.append(gotojail)

       pacificavenue = Property("Pacific Avenue", "property", 32, 300, 200, 150, 26, 130, 390, 900, 1100, 1275, "bank",
                                "green", 0)
       self.boardlist.append(pacificavenue)

       ncarolinaavenue = Property("North Carolina Avenue", "property", 33, 300, 200, 150, 26, 130, 390, 900, 1100,
                                  1275, "bank",
                                  "green", 0)
       self.boardlist.append(ncarolinaavenue)

       cc3 = CCbox("Community Chest", "communitychest", 34)
       self.boardlist.append(cc3)

       pennsylvaniaavenue = Property("Pennsylvania Ave.", "property", 35, 320, 200, 160, 28, 150, 450, 1000, 1200,
                                     1400, "bank",
                                     "green", 0)
       self.boardlist.append(pennsylvaniaavenue)

       rr4 = rrbox("Short Line", "railroad", 36, "bank")
       self.boardlist.append(rr4)

       chance3 = Chancebox("Chance", "chance", 37)
       self.boardlist.append(chance3)

       parkplace = Property("Park Place", "property", 38, 350, 200, 175, 35, 175, 500, 1100, 1300, 1500, "bank",
                            "darkblue", 0)
       self.boardlist.append(parkplace)

       luxurytax = taxbox("Luxury Tax", "taxspace", 39, 75)
       self.boardlist.append(luxurytax)

       boardwalk = Property("Boardwalk", "property", 40, 400, 200, 200, 50, 200, 600, 1400, 1700, 2000, "bank",
                            "darkblue", 0)
       self.boardlist.append(boardwalk)



#make list of community chest cards
    # (self, name, place, money, jailcards, time in jail, dice roll, game piece, secondaccount, user

       self.cclist = []
       comcard1 = "Advance to Go. Collect $200"
       c1 = CommunityChest(comcard1, 1, 0, 0, 0, 0, 0, 0)
       self.cclist.append(c1)

       comcard2 = "Bank error in your favor. Collect $200"
       c2 = CommunityChest(comcard2, 0, 200, 0, 0, 0, 0, 0)
       self.cclist.append(c2)

       comcard3 = "Doctor's fee. Pay $50"
       c3 = CommunityChest(comcard3, 0, 0, 50, 0, 0, 0, 0)
       self.cclist.append(c3)

       comcard4 = "From sale of stock you get $50"
       c4 = CommunityChest(comcard4, 0, 50, 0, 0, 0, 0, 0)
       self.cclist.append(c4)

       comcard5 = "Get out of jail free"
       c5 = CommunityChest(comcard5, 0, 0, 0, 0, 1, 0, 0)
       self.cclist.append(c5)

       comcard6 = "Go to jail. Go directly to jail. Do not pass. Do not collect $200"
       c6 = CommunityChest(comcard6, 0, 0, 0, 0, 0, 1, 0)
       self.cclist.append(c6)

       comcard7 = "Grand opera night. Collect $50 from every player for opening night seats"
       c7 = CommunityChest(comcard7, 0, 0, 0, 0, 0, 0, 50)
       self.cclist.append(c7)

       comcard8 = "Holiday fund matures. Receive $100"
       c8 = CommunityChest(comcard8, 0, 100, 0, 0, 0, 0, 0)
       self.cclist.append(c8)

       comcard9 = "Income tax refund. Collect $20"
       c9 = CommunityChest(comcard9, 0, 20, 0, 0, 0, 0, 0)
       self.cclist.append(c9)

       comcard10 = "It is your birthday. Collect $10"
       c10 = CommunityChest(comcard10, 0, 10, 0, 0, 0, 0, 0)
       self.cclist.append(c10)

       comcard11 = "Life insurance matures. Collect $100"
       c11 = CommunityChest(comcard11, 0, 100, 0, 0, 0, 0, 0)
       self.cclist.append(c11)

       comcard12 = "Pay hospital fees of $100"
       c12 = CommunityChest(comcard12, 0, 0, 100, 0, 0, 0, 0)
       self.cclist.append(c12)

       comcard13 = "From sale of stock you get $50"
       c13 = CommunityChest(comcard13, 0, 50, 0, 0, 0, 0, 0)
       self.cclist.append(c13)

       comcard14 = "You have won second prize in a beauty contest. Collect $10"
       c14 = CommunityChest(comcard14, 0, 50, 0, 0, 0, 0, 0)
       self.cclist.append(c14)

       # make list of chance cards

       self.clist = []
       ccard1 = "Advance to Go. Collect $200"
       c1 = Chance(ccard1, 1, 0, 0, 0, 0, 0, 0)
       self.clist.append(c1)

       ccard2 = "Advance to Illinois Avenue. If you pass Go, collect $200"
       c2 = Chance(ccard2, 25, 0, 0, 0, 0, 0, 0)
       self.clist.append(c2)

       ccard3 = "Bank pays you dividend of $50"
       c3 = Chance(ccard3, 0, 50, 0, 0, 0, 0, 0)
       self.clist.append(c3)

       ccard4 = "Go Back 3 Spaces"
       c4 = Chance(ccard4, 0, 0, 0, 0, 0, 0, 3)
       self.clist.append(c4)

       ccard5 = "Pay poor tax of $15"
       c5 = Chance(ccard5, 0, 0, 12, 0, 0, 0, 0)
       self.clist.append(c5)

       ccard6 = "Take a trip to Reading Railroad–If you pass Go, collect $200"
       c6 = Chance(ccard6, 6, 0, 0, 0, 0, 0, 0)
       self.clist.append(c6)

       ccard7 = "Make general repairs on all your property–For each house pay $25–For each hotel $100"
       c7 = Chance(ccard7, 0, 0, 0, 25, 0, 0, 0)
       self.clist.append(c7)

       ccard8 = "Your building and loan matures—Collect $150"
       c8 = Chance(ccard8, 0, 50, 0, 0, 0, 0, 0)
       self.clist.append(c8)
       # random thing to pick a random cc or c card
       # random.shuffle code ---> stackoverflow.com

       random.shuffle(self.listofplayers)
       random.shuffle(self.cclist)
       random.shuffle(self.clist)








 #time to actually make the game lol
   def game1(self, Player):
       for obj in self.boardlist:
           if isinstance(obj, Property):
               if obj.owner == Player.name:
                   obj.owner = "bank"
                   obj.house = 0
           if isinstance(obj, utility):
               if obj.owner == Player.name:
                   obj.owner = "bank"
                   obj.house = 0
           if isinstance(obj, rrbox):
               if obj.owner == Player.name:
                   obj.owner = "bank"
                   obj.house = 0

   def game2(self, Player, move, var):
       if Player.diceroll == 1:
           Player.secondaccount += 1

       if Player.diceroll == 0:
           Player.secondaccount = 0

       if Player.secondaccount == 3:
           Player.place = 11
           Player.timeinjail = 3
           print(str(Player.name) + " is now in jail!!")

       else:
           nextspot = int(move) + Player.place
           if var == 1:
               nextspot = int(move)
               if Player.place > nextspot:
                   Player.money += int(200)
                   print(Player.name + " has been around once and gets $200")
               Player.place = nextspot

           if nextspot > 39:
               nextspot += -39
               Player.money += int(200)
               print(Player.name + " has been around once and gets $200")
           Player.place = nextspot
           for box in self.boardlist:
               if self.boardlist.index(box) == Player.place:
                   boxnow = box
                   break
           print(Player.name + " is on " + boxnow.name + ".")

           if isinstance(boxnow, Property):
               if boxnow.owner == "bank":
                   if Player.user == 0:
                       for colorlist in Player.newlist:
                           for pp in colorlist:
                               if isinstance(pp, str):
                                   continue
                               if isinstance(pp, Property):
                                   if pp.color == boxnow.color:
                                       if Player.money >= boxnow.price:
                                           Player.newowner(boxnow)
                                           print(str(Player.name) + " for $" + str(boxnow.price) + ".")
                                           break

                       if boxnow.owner == "bank":
                           if Player.money >= boxnow.price:
                               purchase = random.randint(0, 1)
                               if purchase == 1:
                                   Player.newowner(boxnow)
                                   print(str(Player.name) + " has purchased " + str(boxnow.name) + " for $" + str(
                                       boxnow.price) + ".")

                   if Player.user == 1:
                       if Player.money >= boxnow.price:  # if user
                           buy1 = 0
                           while buy1 == 0:
                               choice = input(
                                   "NOBODY OWNS " + str(
                                       boxnow.name) + ". WOULD YOU LIKE TO BUY IT? TYPE YES OR NO")
                               if choice == "YES":
                                   Player.newowner(boxnow)
                                   print("You have purchased " + str(boxnow.name) + " for $" + str(
                                       boxnow.price) + ".")
                                   buy1 = 1
                               if choice == "NO":
                                   buy1 = 1
                               else:
                                   print("Type in YES or NO!!!")

                       else:
                           print("Not enough money, sorry lol.")
               elif boxnow.owner == Player.name:
                   task = "do nothing"
               else:
                   for character in self.listofplayers:  # determine property owner
                       if character.name == boxnow.owner:
                           propowner = character
                   monopoly = 0
                   for colorlist in propowner.newlist:
                       if colorlist:
                           for pp in colorlist:
                               if pp.color == boxnow.color:
                                   if "monopoly" in colorlist:
                                       monopoly = 1
                                       break
                   if monopoly == 1:
                       if boxnow.house == 0:
                           pay = 2 * int(boxnow.rent)
                       elif boxnow.house == 1:
                           pay = int(boxnow.x1)
                       elif boxnow.house == 2:
                           pay = int(boxnow.x2)
                       elif boxnow.house == 3:
                           pay = int(boxnow.x3)
                       elif boxnow.house == 4:
                           pay = int(boxnow.x4)
                       elif boxnow.house == 5:
                           pay = int(boxnow.x5)
                       if Player.money <= pay:
                           propowner.money += Player.money
                           self.game1(Player)
                           print("By landing on " + str(propowner.name) + "'s " + str(
                               boxnow.name) + " with insufficient funds, " + str(
                               Player.name) + " has lost the game.")
                       else:
                           Player.money += -pay
                           propowner.money += pay
                           print(str(Player.name) + " has landed on " + str(propowner.name) + "'s " + str(
                               boxnow.name) + " and pays " + str(pay) + ".")
                   else:
                       pay = int(boxnow.rent)
                       if Player.money <= pay:
                           propowner.money += Player.money
                           self.game1(Player)
                           print("By landing on " + str(propowner.name) + "'s " + str(
                               boxnow.name) + " with insufficient funds, " + str(
                               Player.name) + " has lost the game.")
                       else:
                           Player.money += -pay
                           propowner.money += pay
                           print(str(Player.name) + " has landed on " + str(propowner.name) + "'s " + str(
                               boxnow.name) + " and pays " + str(pay) + ".")

           if isinstance(boxnow, rrbox):
               if boxnow.owner == "bank":
                   if Player.money >= boxnow.price:
                       if Player.user == 0:
                           if len(Player.rrlist) >= 1:
                               Player.newowner(boxnow)
                               print(Player.name + " has purchased " + boxnow.name + "for $" + str(boxnow.price) + ".")
                           else:
                               purchase = random.randint(0, 1)
                               if purchase == 1:
                                   Player.newowner(boxnow)
                                   print(Player.name + " has purchased" + str(boxnow.name) + " for $" + str(
                                       boxnow.price) + ".")

                       else:
                           raiLL = 0
                           while raiLL == 0:
                               choice = input(
                                   "NOBODY OWNS " + str(boxnow.name) + ". WOULD YOU LIKE TO BUY IT? TYPE YES OR NO.")
                               if choice == "YES":
                                   Player.newowner(boxnow)
                                   raiLL = 1
                               elif choice == "NO":
                                   raiLL = 1
                               else:
                                   print("Answer Y or No.")
                   else:
                       print("You need more money to buy this.")
               elif boxnow.owner == Player.name:
                   task = "nothing"
               else:
                   for one in self.listofplayers:
                       if one.name == boxnow.owner:
                           propowner = one
                   if len(propowner.rrlist) == 1:
                       pay = int(boxnow.r1)
                   elif len(propowner.rrlist) == 2:
                       pay = int(boxnow.r2)
                   elif len(propowner.rrlist) == 3:
                       pay = int(boxnow.r3)
                   elif len(propowner.rrlist) == 4:
                       pay = int(boxnow.r4)
                   if Player.money <= pay:
                       propowner.money += Player.money
                       self.game1(Player)
                       print("By landing on " + str(propowner.name) + "'s " + str(
                           boxnow.name) + " with insufficient funds, " + str(Player.name) + " has lost the game.")
                   else:
                       Player.money += -pay
                       propowner.money += pay
                       print(str(Player.name) + " has landed on " + str(propowner.name) + "'s " + str(
                           boxnow.name) + " and pays " + str(pay) + ".")

           if isinstance(boxnow, utility):
               if boxnow.owner == "bank":  # if buyable
                   if Player.money >= boxnow.price:
                       if Player.user == 0:  # if computer
                           if len(Player.utilitylist) >= 1:
                               Player.newowner(boxnow)
                               print(Player.name + " has purchased " + boxnow.name + " for $" + str(
                                   boxnow.price) + ".")
                           else:
                               purchase = random.randint(0, 1)
                               if purchase == 1:
                                   Player.newowner(boxnow)
                                   print(Player.name + " has purchased " + boxnow.name + " for $" + str(
                                       boxnow.price) + ".")
                       elif Player.user == 1:
                           ut = 0
                           while ut == 0:
                               choice = input(
                                   "NOBODY OWNS " + str(boxnow.name) + ". WOULD YOU LIKE TO BUY IT? TYPE YES OR NO.")
                               if choice == "YES":
                                   Player.newowner(boxnow)
                                   ut = 1
                               elif choice == "NO":
                                   ut = 1
                               else:
                                   print("YES OR NO?!?!?!")
                   else:
                       print("YOU DON'T HAVE ENOUGH MONEY TO PURCHACE THIS PROPERTY. TRY AGAIN LATER")
               elif boxnow.owner == Player.name:
                   task = "do nothing"
               else:
                   for person in self.listofplayers:  # determine property owner
                       if person.name == boxnow.owner:
                           propowner = person
                   if len(propowner.utilitylist) == 1:
                       pay = int(boxnow.u1)
                   elif len(propowner.utilitylist) == 2:
                       pay = int(boxnow.u2)
                   if Player.money <= pay:
                       propowner.money += Player.money
                       self.game1(Player)
                       print("By landing on " + str(propowner.name) + "'s " + str(
                           boxnow.name) + " with insufficient funds, " + str(Player.name) + " has lost the game.")
                   else:
                       Player.money += -pay
                       propowner.money += pay
                       print(str(Player.name) + " has landed on " + str(propowner.name) + "'s " + str(
                           boxnow.name) + " and pays " + str(pay) + ".")

           if isinstance(boxnow, taxbox):
               paytax = boxnow.tax
               if Player.money <= paytax:
                   self.game1(Player)
                   print("With insufficient funds to pay the " + str(boxnow.name) + " of " + str(
                       boxnow.tax) + ", " + str(Player.name) + " has lost the game.")
               else:
                   Player.money += -paytax
                   print(str(Player.name) + " has landed on " + str(boxnow.name) + " and pays " + str(paytax) + ".")

           if isinstance(boxnow, Freespacebox):
               print("nothing happens.")

           if isinstance(boxnow, jailbox):
               Player.place = 11
               Player.jailtime = 3
               print(str(Player.name) + " has landed on " + str(boxnow.name) + ". " + str(
                   Player.name) + " is now in JAIL.")

           if isinstance(boxnow, CCbox):
               # pop code attained from stackoverflow
               self.cclist.append(self.cclist.pop(0))
               c = self.cclist[-1]
               print("Community Chest!" + str(Player.name) + "'s card says: " + str(c.description))
               if c.go > 0:
                   self.game2(Player, c.go, 1)
               if c.collect > 0:
                   Player.money += c.collect
               if c.amountdue > 0:
                   Player.money += -c.amountdue
               if c.housecost > 0:
                   Player.money += -c.housecost
               if c.nojail > 0:
                   Player.jailcard += 1
               if c.jail > 0:
                   Player.place = 11
                   Player.timeinjail = 3
                   print(str(Player.name) + " is now in JAIL.")
               if c.collect50d > 0:
                   for i in self.playerlist:
                       if i != Player:
                           if i.money >= 50:
                               i.money += -50
                               Player.money += 50
                           else:
                               Player.money += i.money
                               i.game1()
                               print(i.name + " has insufficient funds to pay the $50, and loses the game.")


           if isinstance(boxnow, Chance):
               self.clist.append(self.clist.pop(0))
               c = self.chancelist[-1]
               print("Chance!" + str(Player.name) + "'s card says: " + str(c.description))
               if c.go > 0:
                   self.game2(Player, c.go, 1)
               if c.collect > 0:
                   Player.money += c.collect
               if c.amountdue > 0:
                   Player.money += -c.amountdue
               if c.housecost > 0:
                   Player.money += -c.housecost
               if c.nojail > 0:
                   Player.jailcard += 1
               if c.gotojail > 0:
                   Player.place = 11
                   Player.timeinjail = 3
                   print(str(Player.name) + " is now in JAIL.")
               if c.goback > 0:
                   self.game2(Player, int(Player.place) - 1, 1)

           if Player.diceroll == 1:
               print(Player.name + " has rolled doubles, and gets to roll again!")
               roll1 = random.randint(1, 6)
               roll2 = random.randint(1, 6)
               print("die 1 roll: " + str(roll1))
               print("die 2 roll: " + str(roll2))
               if roll1 == roll2:
                   Player.diceroll = 1
               else:
                   Player.diceroll = 0
               self.game2(Player, int(roll1 + roll2), 0)

   def beforenext(self, Player):
       if Player.timeinjail > 0:
           if Player.user == 0:
               if Player.jailcard >= 0:
                   Player.jailcard += -1
                   Player.timeinjail = 0
               if Player.money >= 50:
                   Player.money += 50
                   Player.timeinjail = 0
               else:
                   print(Player.name + " attempts to roll doubles to get out of jail.")
                   roll1 = random.randint(1, 6)
                   roll2 = random.randint(1, 6)
                   print("die 1 roll: " + str(roll1))
                   print("die 2 roll: " + str(roll2))

                   if roll1 == roll2:
                       Player.timeinjail = 0

           if Player.user == 1:
               print("You are in Jail.")
               if Player.jailcard >= 0:
                   jailwhile == 0
                   while jailwhile == 0:
                       jailcarduse = input("Do you want to use a jailcard to get out? Type YES or NO.")
                       if jailcarduse == "YES":
                           Player.jailcard += -1
                           Player.timeinjail = 0
                           jailwhile = 1
                       elif jailcarduse == "NO":
                           jailwhile = 1
                       else:
                           print("YES OR NO")

               if Player.money >= 50:
                   jpay = 0
                   while jpay == 0:
                       jailpay = input("Do you want to pay $50 to get out of jail? Type YES or NO.")
                       if jailpay == "NO":
                           jpay = 1
                       if jailroll == "YES":
                           Player.money += -50
                           Player.timeinjail = 0
                       else:
                           print("YES or NO???")

       for colorlist in Player.newlist:
           if "monopoly" in colorlist:
               for property in colorlist:
                   if property.house <= 5:
                       hw = 0
                       while hw == 0:
                           if property.house == 5:
                               hw = 1
                           if Player.money >= property.cost:
                               if Player.user == 0:
                                   Player.money += -property.cost
                                   property.house += 1
                               if Player.user == 1:
                                   rip = input(
                                       "Do you want to buy a house on " + property.name + "? Type YES or NO.")
                                   if rip == "NO":
                                       hw = 1
                                   if rip == "YES":
                                       Player.money += -property.cost
                                       property.house += 1
                                   else:
                                       print("YES OR NO?")
                           else:
                               hw = 1

       if Player.user == 1:

           holder = []
           for colorlist in Player.newlist:
               if colorlist:
                   holder = ["yes"]

           if holder or Player.rrlist or Player.utilitylist:  # DOES THIS WORK?
               mwhile = 0
               print("Do you want to mortgage some property?")
               while mwhile == 0:
                   decision = input("Type YES or NO.")
                   if decision == "YES":
                       m1 = input(
                           "Please type the name of the property you own that you would like to mortgage.")
                       for colorlist in Player.newlist:
                           for pp in colorlist:
                               if pp.name == m1:
                                   colorlist.remove(pp)
                       for box in self.boardlist:
                           if box.name == m1:
                               if box.owner == Player.name:
                                   box.owner = "bank"
                                   box.house = 0
                                   Player.money += box.mortgage
                       print("would you like to mortgage some additional property?")

                   elif decision == "NO":
                       mwhile = 1
                   else:
                       print("YES OR NO???")



def monopoly():
   print("MONOPOLY!")
   beginning = 0
   while beginning == 0:
       np = int(input("How many people would you like to play against? "))
       if np > 0:
           beginning = 0
       else:
           print("Enter a number!!")
       pn = str("Player")
       newboard = board(np, pn)
       pg = 1
       while pg == 1:
           for Player in newboard.listofplayers:
               if len(newboard.listofplayers) == 1:
                   for Player in newboard.listofplayers:
                       print(Player.name + " wins")
                   pg = 0
               print(Player.name + " 's turn")
               if Player.timeinjail > 0:
                   print(Player.name + " is in jail")
               newboard.beforenext(Player)
               print(Player.name + " rolls the dice")
               roll1 = random.randint(1,6)
               roll2 = random.randint(1,6)
               print("roll 1:    " + str(roll1))
               print("roll 2:    " + str(roll2))
               if roll1 == roll2:
                   Player.diceroll = 1
               else:
                   Player.diceroll = 0
               newboard.game2(Player, int(roll1 + roll2), 0)
               print(" ")
               print(" ")


monopoly()








