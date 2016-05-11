import argparse
import socket
import sys
import os
from classes.csv_export import CSVExport
from classes.json_export import JSONExport
from _thread import start_new_thread
from time import sleep

class LightPowertoolServer(object):

    def __init__(self, HOST, PORT, name):
        super(LightPowertoolServer, self).__init__()

        self._HOST = HOST
        self._PORT = PORT
        self._data = []
        self._socket = self.socket
        self._name = name
        self._num = 0

    @property
    def socket(self):
        if hasattr(self, '_socket') and self._socket:
            return self._socket
        try:
            print('Socket initialization...')
            self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._socket.bind((self._HOST, self._PORT))
            print('HOST %s - PORT %s' % (self._HOST, self._PORT))
            self._socket.listen(10)
            print('Socket is listening!')
        except socket.error as msg:
            print('Bind failed. Error Code %s - Message %s' % (str(msg[0]), msg[1]))
            sys.exit()
        return self._socket

    def name_test(self, num):
        return "Test_" + self._name + "_" + str(self._num)

    def test_dir(self, dirname):
        if not os.path.isdir(dirname):
            os.mkdir(dirname)
            os.chdir(dirname)
        else:
            os.chdir(dirname)
            if not os.path.isdir(self._name):
                os.mkdir(self._name)
                os.chdir(self._name)
            else:
                os.chdir(self._name)

    def get_communication(self, conn, addr):
        ip = addr[0]
        port = str(addr[1])
        while True:
            data = conn.recv(1024).decode(encoding='UTF-8').strip()
            data = data.split("-")
            if data and data[0]:
                if data[0] == "FINISHED":
                    csv_file = CSVExport(self.name_test(self._num))
                    csv_file.export_data(self._data)
                    self._num += 1
                    self._data.clear()
                    break
                elif data[0] == "NEW":
                    self._tosave = data[1]
                else:
                    print("%s, from %s on port %s" % (data, ip, port))
                    self._data.append(data)
            else:
                break
        print('Lost connection with %s on port %s' % (ip, port))
        conn.close()

    def run(self):
        print('Running communications...')
        while True:
            # wait to accept a connection - blocking call
            conn, addr = self._socket.accept()
            print('Connected with %s on port %s!' % (addr[0], str(addr[1])))

            start_new_thread(self.get_communication, (conn, addr))

    def shutdown(self):
        print('Socket is closing...')
        self._socket.close()
        csv_file = CSVExport(self.name_test(self._num))
        csv_file.export_data(self._data)

        #json_file = JSONExport(self._tosave)
        #json_file.export(self._data)

def main():
    r"""
    Main program of LightPowertoolServer.

    LightPowertoolServer is a software to communicate\
     between the energy measurement software (LightPowertool)\
     and the tests runner (Calabash).
    """
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="127.0.0.1",
                        help="Server host.")
    parser.add_argument("-p", "--port", type=int, default=8888,
                        help="Port to listen.")
    parser.add_argument("-s", "--sleep", type=int, default=60,
                        help="Time to sleep listening data.")
    parser.add_argument("-n", "--name", type=str,
                        help="Test name.")
    args = parser.parse_args()

    server = LightPowertoolServer(args.host, args.port, args.name)
    # Create the "tests" directory to save the measures 
    server.test_dir("tests")
    start_new_thread(server.run, ())
    # For example, close the socket after 60 running seconds
    sleep(args.sleep)
    server.shutdown()

if __name__ == '__main__':
    main()
