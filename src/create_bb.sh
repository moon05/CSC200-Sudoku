#!/bin/bash
rm data/cnf_files/fstage/fclean/"$1"/*
for var in $(seq 0 "$2")
do
	python sudoku_cnf.py "$1" "$var"
	echo "Staged CNF for Board Size $1 with $var variables"
done	
