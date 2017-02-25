#!/bin/bash
sort -k1 -n summary_results/summary_9.txt > summary_results/temp.txt
rm summary_results/summary_9.txt
mv summary_results/temp.txt summary_results/summary_9.txt

sort -k1 -n summary_results/summary_16.txt > summary_results/temp.txt
rm summary_results/summary_16.txt
mv summary_results/temp.txt summary_results/summary_16.txt
