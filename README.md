#Basic AutoGrader System

##Cloud based scalable auto grader system using Docker.

###Initial setup can be performed like this  

1. Setup t2 Medium Ubuntu Server 16.04 LTS with disk size 20GB using AWS EC2 Service.

        1. Setup new AWS security group with SSH port 22 open from everywhere.
        2. Attempt to SSH to VM using Putty (Make sure you Load and save your PEM key as private key which you need to SSH into VM using putty)
        3. Login via "ubuntu"
        
2. Once on VM, install Python, docker

        sudo apt-get update
        sudo apt-get install build-essential
        sudo apt-get install python-dev
        curl -fsSL https://get.docker.com/ | sudo sh
        sudo usermod -aG docker $(whoami)      
                    <<comment: logout and logback in.>> 
        sudo apt-get install python-pip
        sudo pip install Flask==0.10.1
        
3. Upload the code on AWS Beanstalk if you wish
        
        use this file from codebase- autograder_beanstalk_config.txt