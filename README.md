# aquarium_nano_bootstrap

Ansible scripts codifying the setup of a Aquarium Jetson Nano

## Usage

These scripts assume a relatively current version of `ansible-playbook` has been installed.  


It also assumes SSH access to the Nano.

The script `update.py` is a thin wrapper around ansible:

```
./update.py
```

## Running locally

To run locally on 22.04 Ubuntu systems (for example, Jetpack 6.2), `ansible` must be installed from PPA:

```
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository --yes --update ppa:ansible/ansible
sudo apt install ansible
```

then 

```
./run_local.sh
```
