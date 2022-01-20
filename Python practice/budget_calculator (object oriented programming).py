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
    
    def transfer(self, amount, other_category): #    '''create a withdraw event in the ladger and take money to this category balance to transfer to a new one'''
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to ' + other_category.name)
            other_category.deposit(amount, f'Transfer from ' + self.name)
            return True
        return False
    
    def __str__(self):
        str_top = f'{self.name:*^30}\n'
        lista = ''
        suma = 0
        for e in self.ledger:
            lista += f'{e["description"][0:23]:23}' + f'{e["amount"]:>7.2f}\n'
            suma += e["amount"]

        end = 'Total: ' + str(suma)
        string = str_top + lista + end
        return string

    
    
def create_spend_chart(category_list):
    long = len(category_list)
    total_expenses = 0
    for e in category_list:
        expenses = sum_spend(e)
        total_expenses += expenses
    
    category_names = []
    for e in category_list:
        category_names.append(e.name)
        
    percentages = []
    for e in category_list:
        spend = sum_spend(e)
        percentage = spend / total_expenses * 100
        percentage = truncate(percentage)
        percentages.append(percentage)
        
    title = 'Percentage spent by category\n'
    lines = ""
    i = 10
    while i >= 0:
        if i == 0:
            lines += " "
        lines += str(i * 10) + "| "
        for idx, e in enumerate(category_names):
            if percentages[idx] >= i * 10:
                lines += "o  "
            else:
                lines += "   "           
        lines += "\n " 
        i -= 1
    chart_base = "   "
    for e in category_list:
        chart_base += "---"
    chart_base += "-\n"
    
    labels = "" 
    max_label = max(len(e) for e in category_names)
    j = 0
    while j < max_label:
        labels += "    "
        for e in category_names:
            try:
                letter = " " + str(e[j]) + " "
                labels += letter
            except:
                labels += "   "
        if j < max_label-1:
            labels += " \n" 
        else:
            labels += " "
        j += 1

    output = title + lines + chart_base + labels
    return output
    
    
                
        
       
def sum_spend(category):
    '''
 sum all the money spend in a category form the ladger dictionary but do not include transfereces (which are not money spend)

    '''
    total_expenses = 0
    for e in category.ledger:
            if e['amount'] < 0 and e['description'][0:11] != 'Transfer to':
                total_expenses += e['amount']*(-1)
    return total_expenses
    
      
       
def truncate (num):
    ''' 
    truncate numbers to its nearest 'tens':
        99.9 --> 90
        7,85 --> 0    
    '''
    if num >= 90:
        return 90
    if num >= 80:
        return 80
    if num >= 70:
        return 70
    if num >= 60:
        return 60
    if num >= 50:
        return 50
    if num >= 40:
        return 40
    if num >= 30:
        return 30
    if num >= 20:
        return 20
    if num >= 10:
        return 10
    else:
        return 0
        
        


        
        
        
food = Category('Food')

ropas = Category('Ropas')

food.deposit(1000, 'deposito inicial')

food.get_balance()

prueba = food.get_balance()

food.check_funds(1000)

food.deposit(50, 'porque si')


food.withdraw(950, 'un festin')

food.transfer(50, ropas)

food.check_funds(950)

print(food)

print(ropas)

ropas.withdraw(50, 'una cartera')

lista = [food, ropas]

print(create_spend_chart(lista))
