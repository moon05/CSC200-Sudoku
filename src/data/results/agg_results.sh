#!/bin/bash
total_sat=0
total_solved=0
first_in=0
rm ../summary_results/summary_for_size_"$1".txt
for file in `ls *.sol | sort -V`
do
	num_now=$(python -c "f = '$file'.split('_')[1]; print(f,end='')")
	if [[ "$first_in" != 0 ]]
	then
		if [[ "$num_now" != "$num_prev" ]]
		then	
			ratio=$(python -c "print( int('$total_sat')/int('$total_solved'), end='')")
			printf "$num_now $ratio\n" >> ../summary_results/summary_for_size_"$1".txt
			let total_sat=0
			let total_solved=0
		fi
	fi
	let first_in=1
	num_prev="$num_now"
	sat=$(awk '/^SAT/ {print 1}' "$file")
	total_sat=$((total_sat + sat))
	let total_solved+=1
done
sort -k1 -n ../summary_results/summary_for_size_"$1".txt > ../summary_results/temp.txt
rm ../summary_results/summary_for_size_"$1".txt
mv ../summary_results/temp.txt ../summary_results/summary_for_size_"$1".txt
