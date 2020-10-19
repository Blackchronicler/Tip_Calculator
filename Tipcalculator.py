# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 15:15:06 2020

@author: Ty
"""

### This is a tip calculator
def tipcalculator ():
    mealprice = float(input('How much is the meal?: '))
    tippercent = float(input('How much will you like to tip?: '))
    tipamount = ((tippercent/100) * mealprice )
    bill = (mealprice + tipamount)
    print('Your tip will be' , tipamount , '€')
    print ('Your bill incl. the tip will be' , bill , '€')
    
tipcalculator()