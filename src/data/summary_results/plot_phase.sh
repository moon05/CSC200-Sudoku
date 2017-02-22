#!/bin/bash
#TODO Set this up to graph from the file in this same directory
gnuplot << EOF
#set terminal to save output as picture
#set autoscale ymax
#set size .75 1
set style line 2  lc rgb '#0025ad' lt 1 lw 1.5 # --- blue
set style line 3 lc rgb '#09ad00' lt 1 lw 1.5 # --- green
set style line 4 lc rgb "red" lt 1 lw 1.5 # --- green
set term png
set output 'plots/sat_class.png'
set title '%SAT vs Ratio'
set xlabel 'Ratio'
set ylabel '% SAT'
set grid
set key below
#############
# SAT Graph #
#############
plot "summary_for_size_.txt" using 1:2 title "2 Trials" with lines
EOF
