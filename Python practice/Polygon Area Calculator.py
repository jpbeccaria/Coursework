# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 11:35:55 2022

@author: Juan
"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
        
    def set_width(self, width):
        self.width = width
        
    def set_height(self, height):
        self.height = height
        
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        ans = (self.width ** 2 + self.height ** 2) ** .5
        return ans
        
    def get_picture(self):
        if self.height> 50 or self.width > 50:
            return "Too big for picture."
        picture = ''
        i = 0
        while i < self.height:
            j = 0
            while j < self.width:
                picture += '*'
                j +=1
            picture += '\n'
            i += 1
        return picture
    
    def get_amount_inside(self, new_object):
        times_height = self.height // new_object.height
        times_width = self.width // new_object.width
        return times_height * times_width
        
class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        self.width = side
        self.height = side
        
    def __str__(self):
        return f'Square(side={self.side})'
        
    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side

    def set_width(self, width):
        self.side = width
        self.width = width
        self.height = width
        
    def set_height(self, height):
        self.side = height
        self.height = height
        self.width = height
        
        
        
        
    
        
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
