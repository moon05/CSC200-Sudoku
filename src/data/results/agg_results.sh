#!/bin/bash
total_sat=0
total_solved=0
first_in=0
rm ../summary_results/*.txt
echo "sorting"
for file in `ls *.sol | sort -V`
do
	echo "done sorting"
	num_now=$(python -c "f = '$file'.split('_')[1]; print(f,end='')")
	size=$(python -c "f = '$file'.split('_')[0].replace('r', ''); print(f,end='')")
	if [[ "$first_in" != 0 ]]
	then
		if [[ "$num_now" != "$num_prev" ]]
		then	
			psat=$(python -c "print( int('$total_sat')/int('$total_solved'), end='')")
			ratio=$(python -c "demon=int('$size') * int('$size'); print(int('$num_now')/int(demon), end='')")
			printf "$ratio $psat\n" >> ../summary_results/summary_for_size_"$size".txt
			echo "$ratio $psat\n"
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
sort -k1 -n ../summary_results/summary_for_size_9.txt > ../summary_results/temp.txt
rm ../summary_results/summary_for_size_9.txt
mv ../summary_results/temp.txt ../summary_results/summary_for_size_9.txt

sort -k1 -n ../summary_results/summary_for_size_16.txt > ../summary_results/temp.txt
rm ../summary_results/summary_for_size_16.txt
mv ../summary_results/temp.txt ../summary_results/summary_for_size_16.txt
