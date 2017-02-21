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
set output '../../plots/sat_class.png'
set title 'Class Data: %SAT vs Ratio'
set xlabel 'Ratio'
set ylabel '% SAT'
set grid
set key below
#############
# SAT Graph #
#############
#get a list of all files in directory
file_list=system('ls -1B *.dat')
set yrange[0:1.1]
#loop through and plot all files in directory fpr %sat-ratio
plot for [file in file_list] file u 3:4 smooth csplines with lines t file
clear
#############
# Dec Graph #
#############
set title 'Class Data: Number of Decisions vs Ratio'
set ylabel 'Number of Decisions'
set output '../../plots/dec_class.png'
set yrange[0:850000]
#loop through and plot all files in directory for numdec-ratio
plot for [file in file_list] file u 3:5 smooth csplines with lines t file
clear
#####################
# SAT and Dec Graph #
#####################
#set grid x y2
#set y2range[0:1]
#set y2label "Percent SAT"
#set y2tics .1 nomirror 2
#set title 'Number of Decisions and Percent SAT vs Ratio'
#set ylabel 'Number of Decisions'
#set output '../plots/sat_desc.png'
#loop through and overlay sat and desc plots
#plot for [file in file_list] file u 1:3 smooth csplines with lines t file, for [file in file_list] file u 1:2 axes x1y2 smooth csplines with lines t file
EOF
