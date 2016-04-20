import argparse

from yoctoammeter import YoctoDevice

def main():

    args = argparse

    yocto_device = YoctoDevice()

    print(yocto_device)

    yocto_device.run()

if __name__ == '__main__':
    main()
