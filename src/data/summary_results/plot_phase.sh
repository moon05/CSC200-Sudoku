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
set output 'plots/sat_9.png'
set title '%SAT vs Ratio of Initialized Squares to Board Size'
set xlabel 'Ratio'
set ylabel '% SAT'
set grid
set key below
#############
# SAT Graph #
#############
plot "summary_9.txt" using 1:2 title "2 Trials" with lines
###############
set output 'plots/sat_16.png'
plot "summary_16.txt" using 1:2 title "2 Trials" with lines
##############
set output 'plots/plot_sat_overlap.png'
plot "summary_9.txt" using 1:2 title "9 X 9 500 trials" with lines, "summary_16.txt" using 1:2 title "16 X 16 500 trials" with lines
#############
set title 'Ratio vs Number of Decisions'
set ylabel 'Number of Decisions'
set output 'plots/plot_dec_9.png'
plot "summary_9.txt" using 1:3 title '9 X 9 500 trials' with lines
############
set output 'plots/16_hard.png'
plot "summary_16.txt" using 1:3 title '16 X 16 500 trials' with lines
############
set output 'plots/9_hard.png'
plot "summary_9.txt" using 1:3 title '9 X 9 500 trials' with lines, "summary_16.txt" using 1:3 title '16 X 16 500 trials' with lines
###########
set title 'Hardness Density'
set output 'plots/density.png'
set style fill transparent solid 0.5 noborder
set style circle radius 0.005
plot "density_s_16.txt" u 1:2 title 'Satisfiable Problems' with circles lc rgb "blue", 'density_u_16.txt' u 1:2 title 'Unsatisfiable Problems' with circles lc rgb "red"
set logscale y 10
set output 'plots/density_log.png'
plot "density_s_16.txt" u 1:2 title 'Satisfiable Problems' with circles lc rgb "blue", 'density_u_16.txt' u 1:2 title 'Unsatisfiable Problems' with circles lc rgb "red"
EOF
