import socket
import sys
from _thread import start_new_thread
from time import sleep

class LightPowertoolServer(object):

    def __init__(self, HOST, PORT):
        super(LightPowertoolServer, self).__init__()

        self._HOST = HOST
        self._PORT = PORT
        self._socket = self.socket

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

    def get_communication(self, conn, addr):
        while True:
            data = conn.recv(1024)
            if data:
                print(data)
            else:
                break
        print('Lost connection with %s on port %s' % (addr[0], str(addr[1])))
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

def main():
    server = LightPowertoolServer("127.0.0.1", 8888)
    start_new_thread(server.run, ())
    # For example, close the socket after 60 running seconds
    sleep(60)
    server.shutdown()

if __name__ == '__main__':
    main()
