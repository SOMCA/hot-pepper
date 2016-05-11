#!/bin/bash

count=0

for i in {1..30}
do
		cd /home/antonin/Documents/internship/hot-pepper/
		# RUN CALABASH
		cd scenarios/app_sound_waves/calabash_sound_waves/MIM && calabash-android run /home/antonin/Documents/apps/soundwaves_release.apk&
		cd ../../../
		python3.4 /home/antonin/Documents/internship/hot-pepper/software/lightpowertool_suite/light_powertool.py -n -t 285 -s
		count=$((count+1))
		sleep 10
done
