#!/bin/bash
total_sat=0
total_solved=0
first_in=0
rm ../summary_results/*.txt
echo "sorting"
rm med_dec.txt
touch med_dec.txt
touch scat_9.txt
touch scat_16.txt
rm ../summary_results/desc_*.txt
for file in *.sol
do
	num_now=$(python -c "f = '$file'.split('_')[1]; print(f,end='')")
	size=$(python -c "f = '$file'.split('_')[0].replace('r', ''); print(f,end='')")
	if [[ "$first_in" != 0 ]]
	then
		if [[ "$num_now" != "$num_prev" ]]
		then	
			psat=$(python -c "print( int('$total_sat')/int('$total_solved'), end='')")
			ratio=$(python -c "demon=int('$size') * int('$size'); print(int('$num_now')/int(demon), end='')")
			printf "$ratio $psat\n" >> ../summary_results/summary_for_size_"$size".txt
			med_dec=$(sort -n med_dec.txt | awk '{c[NR]=$1} END {print c[int(NR/2+1)]}')
			rm med_dec.txt
			touch med_dec.txt
			printf "$ratio $med_dec" >> ../summary_results/desc_"$size".txt
			echo "$ratio $psat\n"
			let total_sat=0
			let total_solved=0
		fi
	fi
	let first_in=1
	num_prev="$num_now"
	awk '/decisions/ {print $1}' >> med_dec.txt
	idec=$(awk '/decisions/ {print $1}')
	printf "$ratio $idec" >> scat_"$size".txt
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
