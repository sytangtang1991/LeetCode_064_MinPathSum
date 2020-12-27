#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 20:49:52 2020

@author: yangsong
"""



# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, 
# which minimizes the sum of all numbers along its path.

grid = [[1,3,1],[1,5,1],[4,2,1]]

def minPathSum(grid):
    
    n_row=len(grid)
    n_col=len(grid[0])
    
    for i in range(n_row):
        for j in range(n_col):
            if i==0 and j==0:
                grid[i][j]=grid[i][j]
                # print('i=',i,'j=',j,'output=',grid)
            elif i==0 and j>0:
                grid[i][j]=grid[i][j]+grid[i][j-1]
                # print('i=',i,'j=',j,'output=',grid)
            elif i>0 and j==0:
                grid[i][j]=grid[i][j]+grid[i-1][j]
                # print('i=',i,'j=',j,'output=',grid)
            elif i>0 and j>0:
                grid[i][j]=min(grid[i-1][j],grid[i][j-1])+grid[i][j]
                # print('i=',i,'j=',j,'output=',grid)
    
    return(grid[n_row-1][n_col-1])
  
minPathSum(grid)          