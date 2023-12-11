#!/usr/bin/python

import sys, socket, time

timeout = 5
ip = "host_addr"
port = host_port
prefix = "prefix_here "

string = prefix + "A" * 100

while True:
    try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip, port))
	s.recv(1024)

	print "Fuzzing with {} bytes".format(len(string) - len(prefix))
	s.send(string + "\r\n")
	s.recv(1024)
    except:
	print "Could not connect to " + ip + ":" + str(port)
	sys.exit(0)
    string += 100 * "A"
    time.sleep(1)
