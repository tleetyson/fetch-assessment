# Project Title
The program accepts a single, required input argument to a configuration file path. A well-formed configuration file is a YAML list. Each entry in is converted into an HTTP request (GET or POST) to sent to sent to the URL in each entry

# Setting up git (if you're using a Windows machine)
Follow this guide on downloading git: https://git-scm.com/downloads/win

# Setting up SSH key (if you're using SSH)
Follow the following instructions
1. Generate new SSH key (if you don't already have to): ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
2. Copy the contents of your public SSH key to your clipboard: cat ~/.ssh/id_rsa.pub
3. Verify SSH connection to Github: ssh -T git@github.com 
        (You should be seeing something like "Hi username! You've successfully authenticated, but GitHub does not provide shell access.")


# Pull project from Github
Pull the repo in your terminal using one of the following methods:
1. HTTPS
        i. git clone https://github.com/tleetyson/fetch-assessment.git
2.  SSH
        ii. git clone git@github.com:tleetyson/fetch-assessment.git

# Installing Python
Follow the following steps that correlate to your OS:
1. Windows
        i. Download python following this website: https://www.python.org/downloads/
        ii. Open the downloaded installer file (python-<version>-amd64.exe).
            !!! Important: Check the box that says "Add Python to PATH" before clicking on "Install Now" !!! (This ensures Python is accessible from the command line)
        iii. In the terminal (command prompt), run either of these commands to verify python is installed: "python --version", python3 --version
        iv. In the terminal (command prompt), run either of these commands to verify pip (python's package installer) is installed: 
                "pip --version"
2. Linux/MacOS
        i. Varying Systems
            1. Ubuntu/Debian-based systems: 
                a. run "sudo apt update"
                b. run "sudo apt install python3"
                c. run "sudo apt install python3-pip"
            2. Redhat/CentOS-based systems: 
                a. run "sudo yum update"
                b. run "sudo yum install python3"
                c. run "sudo yum install python3-pip"
        ii. Verify python and pip are installed
            1. run "python3 --version"
            2. run "pip3 --version"

# Install necessary packages
Use pip to install necessary packages for this
    a. pip install -r requirements.txt

# Running the application
Go into the directory and follow the following instructions
    a. Start the application: python3 main.py
    b. Enter in a valid YAML file in your directory (you will be asked for an input until you enter in an existing YAML file that ends with .yml or .yaml)
    c. Stop the application: CTRL + C

# Extra (Dockerizing the application)
1. Follow this link to get started and download Docker Desktop: [#docker-installation-instructions](https://docs.docker.com/get-started/get-docker/?_gl=1*ar2gr2*_gcl_au*MjA0MzExMTA2LjE3Mzk0NTUxMjk.*_ga*ODk3NzMzNTgzLjE3Mzk0NTUxMjk.*_ga_XJWPQMJYHQ*MTczOTQ3NDQ3Ni4yLjEuMTczOTQ3NDUwNy4yOS4wLjA.)
2. Start Docker Desktop
    a. For Windows/MacOs
        i. Open Docker Desktop from Applications, and it will automatically start the Docker daemon.
        ii. Verify Docker installation in command line/terminal: run "docker --version"
        iii. Verify Docker is running: run "docker info"
    b. For Linux
        i. Run the following command: run "sudo systemctl start docker"
        (Optional). Enable Docker to start automatically on boot: run "sudo systemctl enable docker"
        ii. Verify Docker installation: run "docker --version"
        iii. Verify Docker is running: run "sudo systemctl status docker"
3. Creating and running Docker image
    a. Build Docker image in your directory: run "docker build -t my-image-name ."
    b. Check built image: run "docker images"
    c. Run Docker image with correct port: run "docker run -p 443:443 <image-name>"





"








    



        

