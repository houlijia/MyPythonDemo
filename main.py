from testvar import testvar
from testfile import dealwithfile
from testport import *
import socket
import fasteners
import threading
import time

def get_and_bind_freeport(*args):
    freeport = FreePort(start=4000, stop=4009)
    time.sleep(1)
    return freeport.port

def funt():
    from multiprocessing.pool import Pool
    jobs = 200
    p = Pool(jobs)
    ports = p.map(get_and_bind_freeport, range(jobs))
    print(f'[ports]: {ports}')
    #assert len(ports) == len(set(ports))
    p.close()

if __name__ == '__main__':
    funt()
    #dealwithfile()
    #testvar()