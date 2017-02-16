#!/bin/bash
for i in {1..81}
do
   START=$(date +%s)
   python initialize_board.py 9 "$i" $1
   END=$(date +%s)
   DIFF=$(( $END - $START ))
   echo "It took $DIFF seconds to fill "$i" spots"
done
echo "done"
