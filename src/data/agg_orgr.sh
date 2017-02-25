#!/bin/bash
rm summary_results/*.txt
rm med_dec.txt
for directory in org_results/*
do
	#echo "$directory"
	size=$(python -c "f = '$directory'.replace('/','_').split('_')[2][1:]; print(f,end='')")
	#echo "SIZE: $size"
	top=$(python -c "f = '$directory'.replace('/','_').split('_')[3]; print(f,end='')")
	#echo "TOP: $top"
	total_sat=0
	total_solved=0
	touch med_dec.txt
	for file in "$directory"/*
	do
		#echo "FILE: $file"
		ratio=$(python -c "demon=int('$size') * int('$size'); print(int('$top')/int(demon), end='')")
		#echo "RATIO: $ratio"
		sat=$(awk '/^SAT/ {print 1}' "$file")
		#echo "SAT: $sat"
		dec=$(awk '/decisions/ {print $3}' "$file")
		#echo "DECSIONS: $dec"
		printf "$dec \n" >> med_dec.txt
		if [[ "$sat" == 1 ]]; then
			printf "$ratio $dec \n" >> summary_results/density_s_"$size".txt
		else
			printf "$ratio $dec \n" >> summary_results/density_u_"$size".txt
		fi
		echo "$ratio $dec"
		total_sat=$((total_sat + sat))
		let total_solved+=1
	done
	med=$(sort -n med_dec.txt | awk '{c[NR]=$1} END {print c[int(NR/2+1)]}')
	rm med_dec.txt
	psat=$(python -c "print( int('$total_sat')/int('$total_solved'), end='')")
	printf "$ratio $psat $med \n" >> summary_results/summary_"$size".txt
	echo "next directory"
done

sort -k1 -n summary_results/summary_for_size_9.txt > summary_results/temp.txt
rm summary_results/summary_for_size_9.txt
mv summary_results/temp.txt summary_results/summary_for_size_9.txt

sort -k1 -n summary_results/summary_for_size_16.txt > summary_results/temp.txt
rm summary_results/summary_for_size_16.txt
mv summary_results/temp.txt summary_results/summary_for_size_16.txt