###  RabbitMQ Task

First need to install dependencies on ansible host 

    apt-get install sshpass

# To start playbook
 ansible-playbook playbook.yml -i inventor  --vault-password-file vault-pass  --ask-pass

