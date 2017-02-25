#!/bin/bash
for file in *.sol
do
	num_now=$(python -c "f = '$file'.split('_')[1]; print(f,end='')")
	size=$(python -c "f = '$file'.split('_')[0].replace('r', ''); print(f,end='')")
	mv $file ../org_results/r"$size"_"$num_now"
	echo "moved: $file"
done
	