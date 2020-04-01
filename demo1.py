'''
    This file is created using Day 5 assignment
    This file uses pylint, for linting
'''
import math
class BankAccount():
    '''
        This is a class for Bank account assignment
    '''
    def withdraw(self, withdraw_amount):
        '''
            Use this method to withdraw amount
        '''
        if int(withdraw_amount) > 0:
            withdraw_amount = int(withdraw_amount) * -1
        if self.__manage_account(int(withdraw_amount)):
            print("Withdraw Successfull. Current balance is: " + str(self.balance))
            return True
        else:
            print("Check your withdraw amount to not be greater than balance. Please try again. Current balance is: " + str(self.balance))
            return False

    def __init__(self, owner, balance):
        self.owner = str(owner)
        self.balance = int(balance)
        print("Account creation successfull")

    def __manage_account(self, amount):
        '''
            Private method for internal use only
        '''
        if self.balance + amount < 0:
            return False
        else:
            self. balance += amount
            return True

    def deposit(self, deposit_amount):
        '''
            Use this method to deposit amount
        '''
        if int(deposit_amount) < 0:
            deposit_amount = int(deposit_amount) * -1
        if self.__manage_account(int(deposit_amount)):
            print(
                "Amount has been successfully deposited. Final balance is: " + str(self.balance))
            return True
        else:
            print(
                "Deposit unsuccessful, please try again later, current balance is " + str(self.balance))
            return False


class Cone():
    '''
      height: datatype integer, the height of the cone

      radius: datatype integer, the radius of the cone

      self.height: gives you the height

      self.radius: gives you the radius

      self.surface_area_value: gives you the surface_area

      self.volume_value: gives you the volume

      self.surface_area(): calculates and return the surface area

      self.volume: calculates and returns the volume
    '''

    def surface_area(self):
        '''
          Sets and return surface area of the cone
        '''
        self.surface_area_value = math.pi * self.radius * \
            (self.radius + self.side_length)
        return self.surface_area_value

    def volume(self):
        '''
        Sets and returns the volume of the cone
        '''
        self.volume_value = math.pi * (self.radius ** 2) * (self.height / 3)
        return self.volume_value

    def __init__(self, height, radius):
        '''
          height: Height of the cone

          radius: Radius of the cone
        '''
        self.height = int(height)
        self.radius = int(radius)
        self.side_length = math.sqrt(self.height ** 2 + self.radius ** 2)
        self.volume()
        self.surface_area()
