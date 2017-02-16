#!/bin/bash
TRIALS=$1
BSIZE=$2
START_INIT=$3
END_INIT=$4
counter=$3
while [ $counter -lt $END_INIT ]
do
	for trial in {0..$TRIALS}
	do
		FILE=$(python complete_board.py $BSIZE $counter)
		echo "$FILE.txt"
		minisat $FILE > results/r"$BSIZE"-"$TRIALS"-"$counter"-$trial.txt
	done
	let counter+=1
done
