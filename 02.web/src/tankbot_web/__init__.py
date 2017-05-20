#!/usr/bin/env python

import sys
import argparse
from server import server_run

# constant
SERVER_HOST_DEFAULT = "0.0.0.0"
SERVER_PORT_DEFAULT = 6010
PIN_RIGHT_1 = 10
PIN_RIGHT_2 = 12
PIN_LEFT_1 = 11
PIN_LEFT_2 = 13

# main
def main():
    parser = argparse.ArgumentParser(prog="run")
    parser.add_argument("--host", action="store", type=str, dest="host",
        help="Specify the server hos")
    parser.add_argument("--port", action="store", type=int, dest="port",
        help="Specify the server port")  
    parser.add_argument("--pin_right_1", action="store", type=int, dest="pin_right_1",
        help="Specify the Right 1 pin")
    parser.add_argument("--pin_right_2", action="store", type=int, dest="pin_right_2",
        help="Specify the Right 2 pin")  
    parser.add_argument("--pin_left_1", action="store", type=int, dest="pin_left_1",
        help="Specify the Left 1 pin")
    parser.add_argument("--pin_left_2", action="store", type=int, dest="pin_left_2",
        help="Specify the Left 2 pin")
    args = parser.parse_args()
    host = initParam(args.host, SERVER_HOST_DEFAULT)
    port = initParam(args.port, SERVER_PORT_DEFAULT)
    
    pin_right_1 = initParam(args.pin_right_1, PIN_RIGHT_1)
    pin_right_2 = initParam(args.pin_right_2, PIN_RIGHT_2)
    pin_left_1 = initParam(args.pin_left_1, PIN_LEFT_1)
    pin_left_2 = initParam(args.pin_left_2, PIN_LEFT_2)
    server_run(host, port, pin_right_1, pin_right_2, pin_left_1, pin_left_2)

def initParam(param, default):
    if param is not None:
        val = param
    else:
        val = default
    return val

if __name__ == "__main__":
    main()
