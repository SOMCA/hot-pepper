from yoctopuce.yocto_api import YAPI, YRefParam, YModule
from yoctopuce.yocto_current import YCurrent

class YoctoDevice(object):
    """Class to instantiate an ammeter object"""

    @property
    def module(self):
        # check if the module is already instantiated
        if hasattr(self, '_module') and self._module:
            return self._module
        # check if the ammeter is attached by USB
        errmsg = YRefParam()
        if YAPI.RegisterHub("usb", errmsg) != YAPI.SUCCESS:
            raise Exception("Could not register the yocto device with USB connection.")

        ammeter = YCurrent.FirstCurrent()
        # find the ammeter
        if not ammeter:
            raise Exception("Could not find the yocto device.")
        # check if the ammeter is online
        if not ammeter.isOnline():
            raise Exception("Your ammeter device is not currently reachable.")
        # initialize the ammeter and return this one
        self._module = ammeter.get_module()
        return self._module

class YoctoAmmeter(YoctoDevice):
    """Class to manipulate the yoctopuce ammeter"""

    def __init__(self):
        super(YoctoAmmeter, self).__init__()

        try:
            module = self.module
            # get the serial number from the module
            self._serial_number, self._hardware_id, self._logical_name = module.get_serialNumber(), module.get_hardwareId(), module.get_logicalName()
            # check the ammeter
            self._device = YCurrent.FindCurrent(".".join([self._serial_number, 'current1']))
            if not self._device and not self.module.isOnline():
                raise Exception('Could not get sensor device from ' + ammeter_serialnumber)
        except Exception as init_exception:
            raise init_exception

    def __repr__(self):
        ammeter_info = [
            "* Yocto ammeter %r" % self._serial_number,
            "---> Hardware ID: %r" % self._hardware_id,
            "---> Logical name: %r" % self._logical_name,
        ]
        return "\n".join(ammeter_info)
