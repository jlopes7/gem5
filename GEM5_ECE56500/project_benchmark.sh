#!/usr/bin/env bash

set -Eo pipefail

BASEDIR="$(dirname `readlink -e $0`)"
OUTPUTDIR="$BASEDIR/Project_Benchmarks"
OPT="${1:-opt}"

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
	if [ $OPT = "debug" ]
	then	$BASEDIR/build/ARM/gem5.${OPT} --outdir="$CURROUTDIR/$BENCH" --debug-flags=MinorMem,MinorCPU --debug-file=$CURROUTDIR/debug.log $BASEDIR/configs/spec/spec_se.py -b "$BENCH" --maxinsts=10000000 --bp-type=TournamentBP --l1d_size=64kB --l1i_size=16kB --caches --l2cache --cpu-type=MinorCPU 
	else	$BASEDIR/build/ARM/gem5.${OPT} --outdir="$CURROUTDIR/$BENCH" $BASEDIR/configs/spec/spec_se.py -b "$BENCH" --maxinsts=10000000 --bp-type=TournamentBP --l1d_size=64kB --l1i_size=16kB --caches --l2cache --cpu-type=MinorCPU
	fi
	echo "---------------------------------------"
	echo
done

exit 0
