from django.db import models
from django.db import connection
from bearbites.con import getConnection


class Account(models.Model):
    email = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128)
    def __str__(self):
        return self.email

    def get_email(self):
        return self.email
    def set_email( self, mail):
        self.email = mail
    def get_password(self):
        return self.password
    def set_password(self, code):
        self.password = code
    def view_users(self):
        cnxn = getConnection()
        cursor = cnxn.cursor()
        cursor.execute("Exec AllAccounts;")
        return cursor.fetchall()
    def getUserAccount(self, mail, code):
        cnxn = getConnection()
        cursor = cnxn.cursor()
        cursor.execute("EXEC AccountLookup @UserName=admin , @PassCode=testbear;")
        return cursor.fetchone()



# Create your models here.
