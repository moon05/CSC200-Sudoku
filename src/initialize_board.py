# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 11:54:54 2017

@author: Owner
"""
import sys
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

cfile= open("test_c.txt", 'w')
file = open("test.txt", 'w')
def initialize(dim, num_init, god=0):
    #initialize i = zero elements initialized
    i=0
    #while board isn't filled
    while i < num_init:
        #randomly select number between 1 and dim (inclusive) and assign to row
        row = randy(1,len(r_set))
        #randomly select number between 1 and dim (inclusive) and assign to column
        col = randy(1,len(c_set))
        #convert cell to str
        str_cell = str(row) + str(col)
        #check to see that cell is not filled
        if str_cell not in used_cells:
            #add to used cells
            used_cells.add(str_cell)
            #if we are not checking for conflicts
            if god == 0:
                #select a random number between 1 and dim
                value = randy(1,dim)
                #convert row col and value to proper minisat form and add to initialized vector
                v_init.append(row*factor**2 + (col*factor) + (value))
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
    return v_init 

def main(argv):
    values = initialize(int(argv[0]), int(argv[1]), god=int(argv[2]))
    file = open("cnf_files/problem_" + str(dim) + ".txt", 'r')
    complete_file = open("cnf_files/complete_files/board_size" + str(dim) + "/new.txt", 'w')
    lineset = file.readlines()
    for line in lineset:
        complete_file.write(line)
    for each in values:
        complete_file.write(str(each) + " 0\n")
    file.close()
    complete_file.close()
    print("return")
    return complete_file
if __name__ == "__main__":
    main(sys.argv[1:])
