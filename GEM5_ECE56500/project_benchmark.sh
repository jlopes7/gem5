#!/usr/bin/env bash

set -Eo pipefail

BASEDIR="$(dirname `readlink -e $0`)"
OUTPUTDIR="$BASEDIR/Project_Benchmarks"

echo "==========================================================="
echo " PROCESSING PROJECT BENCHMARK"
echo "==========================================================="
echo

declare -a BENCHMARKS=("sjeng" "leslie3d" "lbm" "astar" "milc" "namd")

CURROUTDIR="$OUTPUTDIR/`date +%Y-%m-%d`"
[ -d $CURROUTDIR ] && rm -rf $CURROUTDIR/*
! [ -d $CURROUTDIR ] && mkdir -p $CURROUTDIR

for BENCH in "${BENCHMARKS[@]}"
do	echo " Running benchmark '${BENCH^^}' .-." 
	echo "---------------------------------------"
	$BASEDIR/build/ARM/gem5.opt --outdir="$CURROUTDIR/$BENCH" $BASEDIR/configs/spec/spec_se.py -b "$BENCH" --maxinsts=10000000 --bp-type=TournamentBP --l1d_size=64kB --l1i_size=16kB --caches --l2cache
	echo "---------------------------------------"
	echo
done

exit 0
