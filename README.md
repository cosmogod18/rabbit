#  RabbitMQ Task


### First need to install dependencies on ansible host:

    apt-get install sshpass ansible git -y 
    
### Before playing playbook please add this host's fingerprint to your known_hosts file to manage this host, you can do this with connecting to rabbitmq host only one time needed.
### In ansible host you will get promt something like that:
    
ssh root@192.168.160.41
The authenticity of host '192.168.160.41 (192.168.160.41)' can't be established.
ECDSA key fingerprint is SHA256:lFPSWCcyHmyuKHYVKFzscAkIso8amGSSnQiBKl4mfo0.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.160.41' (ECDSA) to the list of known hosts.

### In ansible host modify inventory file with desired IP address and start playbook with:
    
    ansible-playbook playbook.yml -i inventory  --vault-password-file vault-pass  --ask-pass

