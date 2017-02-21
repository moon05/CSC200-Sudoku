#!/bin/bash
for file in *.txt
do
	ext=$(python -c "ext='$file'.replace('.','_').split('_')[1]; print(ext, end='')")
	compare=check/c_prob_"$ext.txt"
	unix2dos "$compare"
	echo -n "comparing $file with $compare..."
	DIFF=$(diff $compare $file)
	if [ "$DIFF" != "" ]
	then
		echo "DIFFERENT"
	else
		echo "SAME"
	fi
done
