from django.db import models
from django.db import connection
from bearbites._con import getConnection
from bearbites._con import dictfetchall
from restaurant.models import Restaurant
# Create your models here.
class Menu(Restaurant):
    menuID = models.IntegerField()
    

    def get_menuID(self):
        return menuID

    def set_menuID(self,num):
        self.menuID = num

        #Get an Item's price
    def getItemRestaurant(self):
        cnxn = getConnection()
        cursor = cnxn.cursor()
        sql = "Select Restaurant.RestaurantID FROM ((Items inner join  Menu on Items.MenuID = Menu.MenuID ) inner join Restaurant on Menu.RestaurantID = Restaurant.RestaurantID ) WHERE ItemID={}".format(self.itemID)
        cursor.execute(sql)
        results = cursor.fetchall()
        response = results[-1][0]
        cursor.close()
        cnxn.close()
        del cnxn
        return response

    

class MenuItem(Menu):
    
    itemID = models.IntegerField()
    itemName = models.CharField(max_length=128)
    itemType = models.CharField(max_length=128)
    itemDescription = models.CharField(max_length=128)
    itemPrice = models.CharField(max_length=128)
    itemDiscount = models.CharField(max_length=128)
    itemImageURL = models.CharField(max_length=128)

# Getter Methods
    def __str__(self):
        return self.itemName

    def get_itemID(self):
        return self.itemID

    def get_itemName(self):
        return self.itemID

    def get_itemType(self):
        return self.itemType

    def get_itemDescription(self):
        return self.itemDescription

    def get_itemPrice(self):
        return self.itemPrice

    def get_itemDiscount(self):
        return self.itemDiscount

    def get_itemImageURL(self):
        return self.itemImageURL

# Setter Methods
    def set_itemID(self, num):
        self.itemID = num

    def set_itemName(self,name):
        self.itemName = name

    def set_itemType(self,type):
        self.itemType = type

    def set_itemDescription(self,desc):
        self.itemDescription = desc

    def set_itemDiscount(self,dis):
        self.itemDiscount = dis

    def set_itemImageURL(self,link):
        self.itemImageURL = link

## Database Queries

# Item Propogration
    def addMenuItem(self):
        try:
            cnxn = getConnection()
            cursor = cnxn.cursor()
            sql = "" # SQL Query to Execute
            cursor.execute(sql.format()) #Fill the Query with Class Properties
            cnxn.commit()
            cursor.close()
            cnxn.close()
            del cnxn
            response = "Menu Item succefully created"
        except:
            response = "Error creating Menu Item"
        return response

# Item Deletion
    def deleteMenuItem(self):
        try:
            cnxn = getConnection()
            cursor= cnxn.cursor()
            sql = ""
            cursor.execute(sql.format())
            cnxn.commit()
            cursor.close()
            cnxn.close()
            del cnxn
            response = "Menu Item succesfully deleted"
        except:
            response = "Error deleting Menu Item"
        return response

# Item Querying

#Query by Description
    def viewMenuCategory(self):
        cnxn = getConnection()
        cursor = cnxn.cursor()
        sql = "SELECT ItemName,ItemDesc,Price FROM Items WHERE MenuID = {} AND itemType = {};".format(self.menuID,self.itemType)
        cursor.execute(sql)
        return dictfetchall(cursor)
        
#Query All Menu Items
    def viewMenu(self,menu):
        cnxn = getConnection()
        cursor = cnxn.cursor()
        sql = "SELECT ItemName,ItemDesc,Price,ItemURL FROM Items WHERE MenuID = {}".format(menu)
        cursor.execute(sql)
        return dictfetchall(cursor)

#Query All Restaurant Items
    def viewItems(self):
        cnxn = getConnection()
        cursor = cnxn.cursor()
        sql = "EXEC ViewRestaurantsItems @Restaurant= {}".format(self.restaurantID)
        cursor.execute(sql)
        return dictfetchall(cursor)
    
#Get an Item's price
    def getItemPrice(self):
        cnxn = getConnection()
        cursor = cnxn.cursor()
        sql = "Select Price FROM Items WHERE ItemID= {}".format(self.itemID)
        cursor.execute(sql)
        results = cursor.fetchall()
        response = results[-1][0]
        cursor.close()
        cnxn.close()
        del cnxn
        return response

#Get an Item's price
    def getItemRestaurant(self):
        cnxn = getConnection()
        cursor = cnxn.cursor()
        sql = "Select Restaurant.RestaurantID FROM ((Items inner join  Menu on Items.MenuID = Menu.MenuID ) inner join Restaurant on Menu.RestaurantID = Restaurant.RestaurantID ) WHERE ItemID={}".format(self.itemID)
        cursor.execute(sql)
        results = cursor.fetchall()
        response = results[-1][0]
        cursor.close()
        cnxn.close()
        del cnxn
        return response
    