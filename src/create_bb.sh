#!/bin/bash
rm data/cnf_files/fstage/fclean/*
for var in $(seq 0 81)
do
	python sudoku_cnf.py 9 "$var"
done	
