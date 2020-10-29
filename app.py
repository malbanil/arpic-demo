#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on oct 28 2020

@author: albanilm
"""
import time

def main(n):   
    with open('log.txt', 'a') as file:
        print('n:' + str(n) )
        file.write(str(n) + " \n") 
    file.close()


if __name__ == '__main__':
    n = 0
    while True:
        main(n)
        time.sleep(10)
        n = (n + 1)
