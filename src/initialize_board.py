# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 11:54:54 2017

@author: Owner
"""
import sys
import board
from random import randint as randy
from math import sqrt
dim = int(sys.argv[1])
factor = 10
if dim > 9:
    factor = 17
#row set
r_set = [set([i for i in range(1,dim + 1)]) for _ in range(dim)]
#column set
c_set = [set([i for i in range(1,dim + 1)]) for _ in range(dim)]
#block set
b_set = [[set([i for i in range(1,dim + 1)]) for _ in range(int(sqrt(dim)))] for _ in range(int(sqrt(dim)))]
#used cell set
used_cells = set([])
#initialized vector
v_init=[]

#cfile= open("test_c.txt", 'w')
#file = open("test.txt", 'w')
def initialize(dim, num_init, god):
    stop=0
    #initialize i = zero elements initialized
    i=0
    #while board isn't filled
    while i < num_init:
        stop+= 1
        #randomly select number between 1 and dim (inclusive) and assign to row
        row = randy(1,len(r_set))
        #randomly select number between 1 and dim (inclusive) and assign to column
        col = randy(1,len(c_set))
        #convert cell to str
        str_cell = str(row) + str(col)
        #check to see that cell is not filled
        if str_cell not in used_cells:
            #if we are not checking for conflicts
            if god == 0:
                #select a random number between 1 and dim
                value = randy(1,dim)
                #convert row col and value to proper minisat form and add to initialized vector
                v_init.append(row*factor**2 + (col*factor) + (value))
                used_cells.add(str_cell)
                #update initialized amount
                i += 1
            elif god == 1:
                b_division = sqrt(dim)
                r = 0
                row_temp = 0
                while True:
                    if row_temp >= row:
                        break
                    else:
                        row_temp += b_division
                        r += 1
                c = 0
                col_temp = 0
                while True:
                    if col_temp >= col:
                        break
                    else:
                        col_temp += b_division
                        c += 1
                #determine the block the selected cell is in assume we are working with perfect squares (4, 9, 16 ...)
                block = b_set[r-1][c-1]
                # to select a value that is valid we must perform some set operations
                valid_values = set.intersection(r_set[row-1], c_set[col-1], block)
                
                if len(valid_values) != 0:
                    #randomly select a value
                    index = randy(0,len(valid_values)-1)
                    value = list(valid_values)[index]
                
                    #convert row col and value to proper minisat form and add to initialized vector
                    v_init.append(row*factor**2 + col*factor + value)
                    
                
                    str_cell=str(row) + str(col)
                    used_cells.add(str_cell)
                    # remove value from associated sets
                    r_set[row-1].remove(value)
                    c_set[col-1].remove(value)
                    block.remove(value)
                
                    #increment num_init
                    i += 1
        if stop > 1000:
            outsource(r_set, c_set, b_set, factor)
            break
    return v_init 
    
    
def outsource(row_s, col_s, block_s, factor):
    #print(used_cells)
    for each_row in row_s:
        r=1
        for each_rval in list(each_row):
            c=1
            for each_col in col_s:
                str_cell = str(r) + str(c)
                for each_cval in list(each_col):
                    if each_rval == each_cval:
                        br=0
                        bc=0
                        if r < 4:
                            br=0
                        elif r < 7:
                            br=1
                        elif r < 10:
                            br=2
                        if c < 4:
                            bc=0
                        elif c < 7:
                            bc=1
                        elif c < 10:
                            bc=2
                        #print("\n" + str_cell + " is used -->" + str(str_cell in used_cells), end='')
                        if each_rval in block_s[br][bc]:
                            if str_cell not in used_cells:
                          #      print( "... and we are filling it!")
                                v_init.append(r*factor**2 + c*factor + each_rval)
                                used_cells.add(str_cell)
                        #else:
                         #    sys.stdout.write(" ... but block is full!")
                c+=1
            r+=1
                            
def main(argv):
    values = initialize(int(argv[0]), int(argv[1]), int(argv[2]))
    for each in values:
        print(str(each) + " " + str(0))
    b = board.extract(v_init, 9)
   # print()
    #print(len(v_init))
    #print(len(used_cells))
    #for each in b:
     #   print(each)
if __name__ == "__main__":
    main(sys.argv[1:])
