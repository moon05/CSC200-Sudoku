# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 23:04:52 2017

@author: Owner
"""
import sys
board = [[0]*int(sys.argv[1]) for _ in range(int(sys.argv[1]))]
board_T = [[0]*int(sys.argv[1]) for _ in range(int(sys.argv[1]))]
options = set(i for i in range(1,int(sys.argv[1])+1))

row_sets = []
column_sets = []

def extract(file,size=9):
    value = 0
    row = 0
    column = 0
    d=10
    if size != 9:
        d=17
    for entry in file:
        num = int(entry)
        row = int((num - (num % d**2)) / d**2)
        column = int(((num % d**2) - ((num % d**2) % d)) / d)
        value = ((num % d**2) % d)
        place_on_board(value, row, column)
    return board
        
def place_on_board(value, row, column):
    board[row-1][column-1] = value
    board_T[column-1][row-1] = value
    
def collect_sets():
    for row, column in zip(board, board_T):
        row_s = set(row)
        column_s=set(column)
        row_s.discard(0)
        column_s.discard(0)
        row_sets.append(row_s)
        column_sets.append(column_s)
    print(row_sets)
    print(column_sets)

def count_options():
    count = 0
    for row in range(0, int(sys.argv[1])):
        for column in range(0, int(sys.argv[1])):
            count += len(options - (row_sets[row] | column_sets[column]))
    print(count)
def test():
    print(options - (set([1,7,3]) | set([7,4])))
#def main():
    #extract([118,233,246,327,359,372,422,467,554,565,577,641,683,731,786,798,828,835,881,929,974], size=9)
    #for row in board:
        #print(row)
    #collect_sets()
    #count_options()
#if __name__ == "__main__":
    #main(sys.argv[1:])
    #main()