# -----------------------------------------------Scan Open Ports of any Website-----------------------------

from socket import *
import time
class PortScan:
    def portscan(self):

        startTime = time.time()
        print("Example:->https://www.theict.in/")
        target = input('Enter the host website to be scanned: ')
        t_IP = gethostbyname(target)
        print('Starting scan on host: ', t_IP)
        print("Please wait it take some time to Scan Because it Scan all the ports......")

        for i in range(50, 500):
            s = socket(AF_INET, SOCK_STREAM)

            conn = s.connect_ex((t_IP, i))
            if (conn == 0):
                print('Port %d: OPEN' % (i,))
            s.close()
        print('Time taken:', time.time() - startTime)