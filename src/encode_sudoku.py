# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 21:37:19 2017

@author: Owner
"""

# -*- coding: utf-8 -*-
"""
This will convert a given board to cnf
"""
import sys
import math
def rc_cnf(size, out_file):
    column_file = open('test_files/to_compare/col16.txt','w')
    row_file = open('test_files/to_compare/row16.txt','w')
    cell_file = open('test_files/to_compare/cell16.txt','w')
    s = int(size) + 1
    for i in range(1,s):
        for j in range(1,s):
            col = 1
            row_string=''
            col_string=''
            cell_string=''
            for k in range(1,s):
                row_string += str(i) + str(col) + str(j) + " "
                col_string += str(col) + str(i) + str(j) + " "
                cell_string += str(i) + str(k) + str(j) + " "
                col += 1
            out_file.write(col_string + "0\n")
            out_file.write(row_string + "0\n")
            column_file.write(col_string + "0\n")
            row_file.write(row_string + "0\n")
            cell_file.write(cell_string + "0\n")
            
def block_cnf(size, out_file):
    s = int(size) + 1
    block_file = open('test_files/to_compare/block16.txt','w')
    step = int(math.sqrt(int(size)))
    first = 1
    first_temp=first
    mid = 1
    mid_temp=mid
    last = 1
    for b in range(1, s, step):
        for a in range(1, s, step):
            for i in range(1, s):
                block_string=''
                for k in range(1,step+1):
                    for l in range(1,step+1):
                        block_string += str(first) + str(mid) + str(last) + " "
                        mid += 1
                    mid = mid_temp
                    first += 1
                last+= 1
                block_file.write(block_string + "0\n")
                first= first_temp
            last = 1
            mid += step
            mid_temp = mid
        first += step
        first_temp += step
        mid = 1
        mid_temp = mid
            
            
def encode_cnf(size, out_file):
    rc_cnf(size, out_file)
    block_cnf(size, out_file)
def main(argv):
    out_file = open(argv[1], 'w')
    encode_cnf(argv[0], out_file)
         
if __name__ == "__main__":
    main(sys.argv[1:])
