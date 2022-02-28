#  RabbitMQ Task
## Tests was made with clean Debian GNU/Linux 11 (bullseye) installation and ansible 2.9.6.




### First of all install dependencies on ansible host:

    apt-get install sshpass ansible git -y 
    
### Before playing ansible playbook please add this host's fingerprint to your known_hosts file to manage this host, you can do this with ssh connection to rabbitmq host, only one time needed.
### In ansible host you will get promt something like that:
    
    ssh root@192.168.160.41

    The authenticity of host '192.168.160.41 (192.168.160.41)' can't be established.
    ECDSA key fingerprint is SHA256:lFPSWCcyHmyuKHYVKFzscAkIso8amGSSnQiBKl4mfo0.
    Are you sure you want to continue connecting (yes/no/[fingerprint])?
    yes
    Warning: Permanently added '192.168.160.41' (ECDSA) to the list of known hosts.

### Download repo:

    git clone https://github.com/cosmogod18/rabbit.git
    
    cd rabbit/
    

### In ansible host modify inventory file with desired IP address and start playbook with:
    
    ansible-playbook playbook.yml -i inventory  --vault-password-file vault-pass  --ask-pass

### After successful playbook You should access RabbitMQ web interface with default port:
        User: testuser
        password: testuserpassword
        Test_exchange: test_exchange
        Test_queue: test_queue
        Routing_key: test_key
        RabbitMq_msg: 'Hello RabbitMQ :)' TTL 3600sec
        VirtualHost: myvirtualhost
        http://x.x.x.x:15671
