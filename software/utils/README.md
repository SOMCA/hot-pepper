Scripts
=======

How to use them?

* ```app_instrumentation_*.py```  
	Please to use the [Firefox-OS Powertool](https://github.com/k0pernicus/fxos-powertool) software with your ammeter.  
	Get the application package name to test, and just add as argument this one and the output directory to store results
	*Example*: ```python3.4 app_instrumentation_robotium.py --app jackpal.androidterm -o /home/user/output_directory -b 1 -n 11```
*	```get_stats_from.py```  
	Unzip the directory you want to get stats, and just add as argument the path of the directory  
	*Example*: ```python3.4 get_stats_from.py -p the/directory/which/contains/all/tests/directories```