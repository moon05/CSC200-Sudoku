# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 19:51:49 2017

@author: Owner
"""

import math
import sys
import itertools as it
ext=str(sys.argv[1])
out_file = open('cnf_files/problem_'+ext+'.txt','w')
'''
cell_file = open('test_files/to_compare/cnf_cell'+ext+'.txt','w')
row_file = open('test_files/to_compare/cnf_row'+ext+'.txt','w')
column_file = open('test_files/to_compare/cnf_col'+ext+'.txt','w')
block_file = open('test_files/to_compare/cnf_block'+ext+'.txt','w')
'''
def cells(size,m):
    size=int(size)+1
    for r in range(1,size):
        for v in range(1,size):
            line=''
            for column in range(1,size):
                value = m**2*r + m*v + column
                #cell_file.write(str(value) + " ")
                line = line + str(value) + " "
            #cell_file.write("0\r")
            out_file.write(line + "0\n")
            #write_negations(negate(line), cell_file)
            write_negations(negate(line), out_file)
            
def rows(size,m):
    size=int(size)+1
    for r in range(1,size):
        for v in range(1,size):
            line=''
            for column in range(1,size):
                value = m**2*r + m*column + v
                #row_file.write(str(value) + " ")
                line = line + str(value) + " "
            #row_file.write("0\r")
            out_file.write(line + "0\n")
            #write_negations(negate(line), row_file)
            write_negations(negate(line), out_file)

def columns(size,m):
    size=int(size)+1
    for r in range(1,size):
        for v in range(1,size):
            line=''
            for column in range(1,size):
                value = m**2*column + m*r + v
                #column_file.write(str(value) + " ")
                line = line + str(value) + " "
            #column_file.write("0\r")
            out_file.write(line + "0\n")
            #write_negations(negate(line), column_file)
            write_negations(negate(line), out_file)
            
def block(size, m):
    s = int(size) + 1
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
                        value = m**2*first + m*mid + last
                        block_string = block_string + str(value) + " " 
                        mid += 1
                    mid = mid_temp
                    first += 1
                last+= 1
                out_file.write(block_string + "0\n")
                #write_negations(negate(block_string), block_file)
                write_negations(negate(block_string), out_file)
                first= first_temp
            last = 1
            mid += step
            mid_temp = mid
        first += step
        first_temp += step
        mid = 1
        mid_temp = mid

def write_negations(neg_list, file):
    for i in neg_list:
        clause = ''
        for j in i:
            clause = clause + j + " "
        #print(clause)
        file.write(clause + "0\n")

def negate(clause):
    #print(clause)
    literals = clause.split(" ")[:-1]
    neg_lit = []
    negation = "-"
    for each_literal in literals:
        each_literal = negation + each_literal
        neg_lit.append(each_literal)
        
    return it.combinations(neg_lit, 2)
    
def main(argv):
    if int(argv[0]) > 9:
        m = 17
    else:
        m = 10
    cells(argv[0], m)
    block(argv[0],m)
    rows(argv[0], m)
    columns(argv[0], m)
if __name__ == "__main__":
    main(sys.argv[1:])
