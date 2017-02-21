#!/bin/bash
# ./play_sudoku.sh <trials per initvar> <board size> <start varnum> <end varnum>
TRIALS=$1
BSIZE=$2
START_INIT=$3
END_INIT=$4
CHECK=$5
counter=$3
rm data/cnf_files/fstage/frun/*.cnf
rm data/results/*.sol
while [ $counter -le $END_INIT ]
do
	for trial in $(seq 1 $TRIALS)
	do
		touch temp.txt
		python initialize_board.py "$BSIZE" "$counter" "$CHECK" >temp.txt
		actual_init=$(wc -l < temp.txt)
		echo "tried: $counter -> got: $actual_init"
		cp data/cnf_files/fstage/fclean/problem_"$2"_"$actual_init".txt data/cnf_files/fstage/frun/problem_"$2"_"$actual_init"_"$trial".cnf 
		#echo $'\r' >> data/cnf_files/fstage/frun/problem_"$2"_"$counter"_"$trial".txt
		while read line; do
			echo "$line" >> data/cnf_files/fstage/frun/problem_"$2"_"$actual_init"_"$trial".cnf
		done <temp.txt
		rm temp.txt
		minisat data/cnf_files/fstage/frun/problem_"$2"_"$actual_init"_"$trial".cnf > data/results/r"$BSIZE"_"$actual_init"_"$TRIALS"_"$trial".sol
		echo r"$BSIZE"_"$actual_init"_"$TRIALS"_"$trial".sol
	done
	let counter+=1
done
