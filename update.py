#!/usr/bin/env python3
#
# This is really a glorified shell script, but I wanted to use argparse
#

import argparse
import subprocess
from pathlib import Path

if __name__=="__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("hosts", default=["all"], nargs='*', help="Hosts to update")

    parser.add_argument("-p", "--ask-pass", action="store_true", help="Ask for SSH password.  If _not_ specified, assumes pubkey based authentication.")

    args = parser.parse_args()

    ansible_cmd = ["ansible-playbook", "-vvv", "-i", "inventory.yml", "ansible.yml", "--ask-become-pass"]

    if args.ask_pass:
        ansible_cmd += ["--ask-pass"]

    for host in args.hosts:
        ansible_cmd += ("-l", host)

    print(f'Running: {ansible_cmd}')
    subprocess.run(ansible_cmd)
