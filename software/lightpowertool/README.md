# Light Powertool

**LightPowertool** is a software to measure automatically the energy consumption
of electronic devices.  
This software has been developed to have a simply measure the energy consumption of a connected device, for a given during time (for example, a smartphone).

***Notice***: **LightPowertool** is a light version of the powerfull [FxOS-Powertool](https://github.com/JonHylands/fxos-powertool) program. We are NOT affliated with Mozilla.

## How to use it ?

### LightPowertool

Please to install the Python Yoctopuce library from the [public and official Yoctopuce website](http://www.yoctopuce.com/FR/libraries.php), or with Pypi:  
```
pip3 install yoctopuce
```

Go to the main directory (```software/light_powertool/```), plug your Yoctopuce ammeter as an USB device, and simply launch the program:  
```
python3.4 light_powertool
```

#### Arguments

```
usage: light_powertool.py [-h] [-f FRAMERATE] [-o OUTPUT] [-s] [-t TIME]

optional arguments:
  -h, --help            show this help message and exit
  -f FRAMERATE, --framerate FRAMERATE
                        Give to the main program the framerate.
  -o OUTPUT, --output OUTPUT
                        Give an output file name to store measured values.
  -s, --statistics      Ask to output basic statistics (mean, median,
                        pvariance,...) on measured values.
  -t TIME, --time TIME  Due time to measure data.
```

### LightPowertoolServer

**LightPowertoolServer** is a local server to receive some informations from the **LightPowertool** software, and save it into a CSV file (for example a list of measures and timestamps).  
You can use it by launching it with:
```
python3.4 light_powertool_server.py
```

#### Arguments

```
usage: light_powertool_server.py [-h] [--host HOST] [-p PORT] [-s SLEEP]

optional arguments:
  -h, --help            show this help message and exit
  --host HOST           Server host.
  -p PORT, --port PORT  Port to listen.
  -s SLEEP, --sleep SLEEP
                        Time to sleep listening data.
```

## Contributing

**LightPowertool** is still in development.  
Found a bug? We'd love to know about it!  
Please report all issues on the github issue tracker.

## License

**LightPowertool** is primarily distributed under the terms of the AGPL license.
