import getpass
import random
import socket
import subprocess
import threading
import time

seq_finder = None
prime_finder = None

def feet_to_miles(feet):
    return "{0} miles".format(float(feet) / 5280)

def hal_20():
    return "I'm afraid I can't do that {0}".format(getpass.getuser())

def get_git_branch():
    try:
        process = subprocess.Popen(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], stdout=subprocess.PIPE)
        output = process.communicate()[0]
    except:
        return "Unknown"

    if not output:
        return "Unknown"
    return output.strip()

def get_git_url():
    try:
        process = subprocess.Popen(['git', 'config', '--get', 'remote.origin.url'], stdout=subprocess.PIPE)
        output = process.communicate()[0]
    except:
        return "Unknown"

    if not output:
        return "Unknown"
    return output.strip()

def get_other_users():
    try:
        host = '192.168.64.3'
        port = 1337

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.send('Who?')
        data = s.recv(255)
        s.close()
        return data.split('$')

    except:
        return "IT'S A TRAAAPPPP"


class FibSeqFinder(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(FibSeqFinder, self).__init__(*args, **kwargs)
        self.sequence = [0, 1]
        self._stop = threading.Event()
        self.num_indexes = 0

    def stop(self):
        self._stop.set()

    def run(self):
        self.num_indexes = 0
        while not self._stop.isSet() and self.num_indexes <= 1000:
            self.sequence.append(self.sequence[-1] + self.sequence[-2])
            self.num_indexes += 1
            time.sleep(.04)

def get_fibonacci_seq(index):
    index = int(index)
    global seq_finder
    if seq_finder is None:
        
        seq_finder = FibSeqFinder()
        seq_finder.start()

    if index > seq_finder.num_indexes:
        value = random.randint(0, 9)
        if value >= 4:
            return "Thinking..."
        elif value > 1:
            return "One second"
        else:
            return "cool your jets"
    else:
        return seq_finder.sequence[index]

def get_hdd_access_time():
    file = open('testFile.txt', 'r+')
    t0 = time.clock()
    print file.read()
    t1 = time.clock() - t0
    print t1
    file.seek(0)
    #file.cache_clear()
    t0 = time.clock()
    print file.read()
    t2 = time.clock() - t0
    print t2        #make sure t2<t1
                    #should NOT use cache for finding t1
    return t1

class PrimeFinder(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(PrimeFinder, self).__init__(*args, **kwargs)
        self.primes = [2]
        self._stop = threading.Event()
        self.num_indexes = 1
        self.current = 3
        self.check = 1
        self.divisors = 0

    def stop(self):
        self._stop.set()

    def run(self):
        self.num_indexes = 0
        while not self._stop.isSet() and self.num_indexes <= 100:
            
            while((self.check < self.current) & (self.divisors < 2)):
                if(self.current%self.check == 0):
                    self.divisors += 1
                self.check += 2

            if((self.check == self.current) & (self.divisors == 1)):
                self.primes.append(self.current)
                self.num_indexes += 1
            self.current += 2
            self.check = 1
            self.divisors = 0

def get_prime_num(index):
    index = int(index-1)
    global prime_finder
    if prime_finder is None:
        
        prime_finder = PrimeFinder()
        prime_finder.start()

    if index > prime_finder.num_indexes:
        return "Thinking..."
    else:
        return prime_finder.primes[index]

