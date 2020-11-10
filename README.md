# osAviController

## Goals
Spin up Avi Controller in OpenStack
 
## Prerequisites:
- Make sure Ansible is installed in the orchestrator VM with OpenStack endpoints access
- Make sure environment variables with OS credentials are present

## Environment:

### Ansible

```
ansible 2.9.12
  config file = None
  configured module search path = ['/home/nic/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /home/nic/.local/lib/python3.8/site-packages/ansible
  executable location = /home/nic/.local/bin/ansible
  python version = 3.8.2 (default, Jul 16 2020, 14:00:26) [GCC 9.3.0]
```

## Run the playbook:
```
ansible-playbook main.yml
```
