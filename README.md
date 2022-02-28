#  RabbitMQ Task


### First need to install dependencies on ansible host:

    apt-get install sshpass

### Modify inventory file with desired IP address and start playbook with:
    
    ansible-playbook playbook.yml -i inventor  --vault-password-file vault-pass  --ask-pass

