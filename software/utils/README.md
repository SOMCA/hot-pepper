# Scripts

## app\_instrumentation\_*.py  
Please to use [our tool](../lightpowertool) or the [Firefox-OS Powertool](https://github.com/k0pernicus/fxos-powertool) software with your ammeter.  
Get the application package name to test, and just add as argument this one and the output directory to store results

Example: ```python3.4 app_instrumentation_robotium.py --app jackpal.androidterm -o /home/user/output_directory -b 1 -n 11```

## display_results.py
Launch this script to get a view of your results to compare applications with different code smells.  
The repository given as parameter must contains all your results for all code smells, and a single file for each code smell which is the merged results (```merge_NOR.csv``` for example).  
You can limit the view until a unique value, using the ```limit``` option.

Example: ```python3.4 display_results.py -p /home/user/my_results```

## display_simple_results.py
Launch this script to get a view of your results for only one code smell.  
The repository given as parameter must contains all tests, for a given and unique code smell.

Example: ```python3.4 display_simple_results.py -p /home/user/my_results_for_this_code_smell```

## get_stats_from.py  
Unzip the directory you want to get stats, and just add as argument the path of the directory  

Example: ```python3.4 get_stats_from.py -p the/directory/which/contains/all/tests/directories```

## mannwhitney_cliffdelta.r
Single R script to compute Mann-Whitney and Cliff-Delta on data.

## merge_results.py
Script to merge your tests for a single code smell, to obtain only one file which contains average values for all tests.

Example: ```python3.4 merge_results.py -p the/directory/which/contains/my/tests/directories -s IGS```
