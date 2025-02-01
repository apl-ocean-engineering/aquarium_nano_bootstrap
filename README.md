# aquarium_nano_bootstrap

Ansible scripts codifying the setup of a Aquarium Jetson Nano

## Usage

These scripts assume `ansible-playbook` has been installed.  On a reasonably current Ubuntu system, `apt-get install ansible` should be enough. 

It also assumes SSH access to the Nano.

The script `update.py` is a thin wrapper around ansible:

```
./update.py
```
