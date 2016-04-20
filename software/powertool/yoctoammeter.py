from yoctopuce.yocto_api import YAPI, YRefParam, YModule
from yoctopuce.yocto_current import YCurrent

class YoctoDevice(object):
    """Class to instantiate an ammeter device"""

    def __init__(self):
        super(YoctoDevice, self).__init__()

        try:
            # check the ammeter
            self._device = YCurrent.FindCurrent(".".join([self.serialNumber, 'current1']))
            if not self._device and not self.module.isOnline():
                raise Exception('Could not get sensor device from ' + ammeter_serialnumber)
        except Exception as init_exception:
            raise init_exception

    def __repr__(self):
        ammeter_info = [
            "* Yocto ammeter %r" % self.serialNumber,
            "---> Hardware ID: %r" % self.hardwareId,
            "---> Logical name: %r" % self.logicalName,
        ]
        return "\n".join(ammeter_info)

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

    @property
    def serialNumber(self):
        if hasattr(self, '_serial_number') and self._serial_number:
            return self._serial_number
        self._serial_number = self.module.get_serialNumber()
        return self._serial_number

    @property
    def hardwareId(self):
        if hasattr(self, '_hardware_id') and self._hardware_id:
            return self._hardware_id
        self._hardware_id = self.module.get_hardwareId()
        return self._hardware_id

    @property
    def logicalName(self):
        if hasattr(self, '_logical_name') and self._logical_name:
            return self._logical_name
        self._logical_name = self.module.get_logicalName()
        return self._logical_name
