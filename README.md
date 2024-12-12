## GEM 5 for LVPT, CLT and VCU Simulations
This is the gem5 simulator adaption for ECE565-CA to use Load Value Prediction (LVP)

The main website can be found at http://www.gem5.org

To run the configured Benchmarks (Spec-2017) using LVPT with LCT and CVU:
```shell
./project_benchmark.sh 2
```

To run it in debug mode
```shell
./project_benchmark.sh 2 debug
```

The inital reports are placed within the folder: `simulation_results`. This include the statistics from the simulation running with configured LCT of 2 bits and Matlabs files as plotted images.
