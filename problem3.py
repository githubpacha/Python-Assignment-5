#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 13:33:24 2021

@author: home
"""

N = '\033[0m'  
R = '\033[0;31m'
B = '\033[0;34m'
G = '\033[0;32m'
Y = '\033[1;33m'
W = '\033[1;37m'

choice = 'y'

while choice != 'n':
    print('\n\t\t{}MENU{}'.format(Y,N))
    print('{}1. Chicken Strips - $3.50'.format(G))
    print('2. French Fries - $2.50')
    print('3. Hamburger - $4.00')
    print('4. Hotdog - $3.50')
    print('5. Large Drink - $1.75')
    print('6. Medium Drink - $1.50')
    print('7. Milk Shake - $2.25')
    print('8. Salad - $3.75')
    print('9. Small Drink - $1.25{}'.format(N))
    costs = [3.50,2.50,4.00,3.50,
             1.75,1.50,2.25,3.75,1.25]
    order = input('Your order: ')
    if len(order) != 0:
        total = 0
        for i in order:
            total += costs[int(i)-1]
        print('** It Costs \033[1;37m $%.2f \033[0m**' %total)
        print('** Items:', len(order),'**')
    
    else:
        print("{}** You haven't ordered anything! **{}".format(B,N))
    choice = input('Still any to order? [y]es / [n]o : ')
    if choice=='n':
        print('\n{}Thankyou! Visit Again!{}'.format(Y,N))
        