# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 14:52:13 2021

@author: user
"""
import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
  
def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else: 
        return 1
    
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1 
    
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

def full_adder(x1, x2, x3):
    #sum
    s1 = XOR(x1, x2)
    _sum = XOR(s1, x3)
    
    #carry
    c1 = AND(s1, x3)
    c2 = AND(x1, x2)
    _carry = OR(c1, c2)
    
    return _sum, _carry

#TEST
print("입력\t\t\tSum, Carry")
print('(0,0,0) => ', full_adder(0,0,0))
print('(0,0,1) => ', full_adder(0,0,1))
print('(0,1,0) => ', full_adder(0,1,0))
print('(0,1,1) => ', full_adder(0,1,1))
print('(1,0,0) => ', full_adder(1,0,0))
print('(1,0,1) => ', full_adder(1,0,1))
print('(1,1,0) => ', full_adder(1,1,0))
print('(1,1,1) => ', full_adder(1,1,1))