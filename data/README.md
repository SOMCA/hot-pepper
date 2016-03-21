Each compressed file represents the energy consumption of an Android application, on 30 runs.  

Name of the compressed file: ```name.of.the.test.package-X.zip```.  

```X``` can be:
*	```R.IGS```, for a refactored Android application (here for the *IGS* code smell),
*	```NR```, for a no-refactored Android application.

This compressed file contains 30 directories (for 30 runs), and each one contains one single CSV file (the energy consumption - mA).
