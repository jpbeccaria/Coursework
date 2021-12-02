# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 12:28:46 2021

@author: Juan
"""

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        
    def deposit(self, amount, description = ''):
        self.ledger.append({'amount': amount, "description" : description})
        
    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({'amount': amount * -1, "description" : description})
            return True
        return False
        
    def get_balance(self):
        balance = 0
        for e in self.ledger:
            balance += e['amount']
        return balance
    
    def check_funds(self, expense):     
        if self.get_balance() >= expense:
            return True
        return False
    
    def ladger(self):
        lista = self.ledger
        return lista
    
    def transfer(self, other_category, amount): #    '''create a withdraw event in the ladger and take money to this category balance to transfer to a new one'''
    if self.check_funds(amount):
        self.withdraw(amount, f'Transfer to {other_category}')
        other_category.deposit(amount, f'Transfer from {self}')
        return True
    return False
        
       
       
      
       
      
       
      

       
       
     
        
        
        
        
        
food = Category('Food')

food.deposit(1000, 'deposito inicial')

food.get_balance()

food.check_funds(1000)

food.deposit(50, 'porque si')

holis = food.ladger()

food.withdraw(950, 'una cartera')

food.check_funds(950)

