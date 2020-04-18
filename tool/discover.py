#!/usr/bin/env python3
import os
import socket    
import multiprocessing
import subprocess
import os


def pinger(job_q, results_q):
    """
    Do Ping
    :param job_q:
    :param results_q:
    :return:
    """
    DEVNULL = open(os.devnull, 'w')
    while True:

        ip = job_q.get()

        if ip is None:
            break

        try:
            subprocess.check_call(['ping', '-c1', ip],
                                  stdout=DEVNULL)
            results_q.put(ip)
        except:
            pass


def get_my_ip():
    """
    Find my IP address
    :return:
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


def map_network(pool_size=255):
    """
    Maps the network
    :param pool_size: amount of parallel ping processes
    :return: list of valid ip addresses
    """

    ip_list = list()

    # get my IP and compose a base like 192.168.1.xxx
    ip_parts = get_my_ip().split('.')
    base_ip = ip_parts[0] + '.' + ip_parts[1] + '.' + ip_parts[2] + '.'

    # prepare the jobs queue
    jobs = multiprocessing.Queue()
    results = multiprocessing.Queue()

    pool = [multiprocessing.Process(target=pinger, args=(jobs, results)) for i in range(pool_size)]

    for p in pool:
        p.start()

    # cue hte ping processes
    for i in range(2, 255):
        jobs.put(base_ip + '{0}'.format(i))

    for p in pool:
        jobs.put(None)

    for p in pool:
        p.join()

    # collect he results
    while not results.empty():
        ip = results.get()
        ip_list.append(ip)

    return ip_list


def run():
    rows, columns = os.popen('stty size', 'r').read().split()
    rows = int(rows)
    str1 = "Active Connections "
    t1 = "="*(len(str1)+2)
    t2 = t1.center(rows*2)
    str1 = str1.center(rows*2)
    print('Mapping...')
    listed = map_network()
    print(t2)
    print("\33[1;92m",str1,"\33[1;00m")
    for lst in listed:
        lst1 = str(lst)
        lst1 ="\33[92m [*] \33[00m" + lst1
        rw = rows *2 + 6
        lst1 = lst1.center(rw)
        print(" " + lst1)    
    print(t2)

