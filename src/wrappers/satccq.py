#!/usr/bin/env python

from subprocess import check_call

import arg_parser
import context
from helpers import kernel_ctl


def setup_satcc():
    # add satcc to kernel-allowed congestion control list
    kernel_ctl.enable_congestion_control('satcc')


def main():
    args = arg_parser.receiver_first()

    if args.option == 'deps':
        print 'iperf'
        return

    if args.option == 'setup_after_reboot':
        setup_satcc()
        return

    if args.option == 'receiver':
        cmd = ['iperf', '-Z', 'satcc', '-s', '-p', args.port]
        check_call(cmd)
        return

    if args.option == 'sender':
        cmd = ['iperf', '-Z', 'satcc', '-c', args.ip, '-p', args.port,
               '-t', '75']
        check_call(cmd)
        return


if __name__ == '__main__':
    main()
